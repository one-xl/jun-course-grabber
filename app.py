import sys
import os

print("==================================================")
print("  JNU Course Grabber 正在释放并加载核心组件...")
print("  程序体积较大，由于底层环境配置，初次启动约需 5~15 秒，请耐心等待！")
print("==================================================")

import json
import time
import threading
import queue
import urllib.parse
from datetime import datetime
from flask import Flask, render_template, request, jsonify, Response
import requests
import requests
from playwright.sync_api import sync_playwright
import sys

time_session = requests.Session()

def get_resource_path(relative_path):
    """获取随包资源文件路径（如 templates）"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), relative_path)

def get_data_path(filename):
    """获取数据保存路径（总是存放在可执行文件所在目录，而不是临时目录）"""
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, filename)

app = Flask(__name__, template_folder=get_resource_path('templates'))

# ==========================================
# 全局状态字典
# ==========================================
STATE = {
    "is_logged_in": False,
    "is_grabbing": False,
    "token": "",
    "cookie": "",
    "studentCode": "",
    "electiveBatchCode": "",
    "campus": "2",
    "isMajor": "1",
    "captured_courses": [],   # 抓取到的课程列表
    "selected_targets": [],   # 用户勾选的目标课程
    "logs": queue.Queue(),    # 日志队列
    "cmd_queue": queue.Queue(),  # 发包指令队列
    "resp_queue": queue.Queue(), # 发包结果队列
    "async_results_queue": queue.Queue(),
    "online_users_count": "--",
    "time_offset": 0,
    "grab_thread": None,
    "stop_event": threading.Event(),
    "waitlist_targets": {}, # 存储正在候补的课程ID -> 课程信息的映射
    "waitlist_thread": None,
    "waitlist_stop_event": threading.Event(),
    "concurrency": 1
}

# 基础 URL
BASE_URL = "https://jwxk.jnu.edu.cn"
VOLUNTEER_URL = f"{BASE_URL}/xsxkapp/sys/xsxkapp/elective/volunteer.do"

# ==========================================
# 日志处理
# ==========================================
def push_log(msg: str, level: str = "info"):
    """向前端推送日志"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    log_entry = {"time": timestamp, "msg": msg, "level": level}
    print(f"[{level.upper()}] {msg}")
    STATE["logs"].put(log_entry)

# ==========================================
# Playwright 拦截与提取模块
# ==========================================
def run_playwright_login():
    """在后台线程中运行 Playwright 启动浏览器并抓包"""
    push_log("正在启动浏览器模块...", "info")
    try:
        with sync_playwright() as p:
            # 启动浏览器 (可见)
            # 伪装正常中文用户时区和语言环境，解决易盾滑块风控报错
            try:
                push_log("正在尝试唤起系统 Edge 浏览器...", "info")
                browser = p.chromium.launch(
                    channel="msedge",
                    headless=False, 
                    args=[
                        '--no-proxy-server',
                        '--disable-blink-features=AutomationControlled'
                    ]
                )
            except Exception as e:
                push_log("找不到系统 Edge 浏览器，尝试使用 Chrome...", "warn")
                browser = p.chromium.launch(
                    channel="chrome",
                    headless=False, 
                    args=[
                        '--no-proxy-server',
                        '--disable-blink-features=AutomationControlled'
                    ]
                )
                
            context = browser.new_context(
                locale='zh-CN',
                timezone_id='Asia/Shanghai'
            )
            page = context.new_page()

            push_log("请在弹出的浏览器中完成登录，并进入选课页面", "warn")
            push_log("提示：在选课页面随便点击一下课程类别（如专业选修），我会自动捕获课程列表！", "warn")
            # --- 网络请求拦截逻辑 ---
            def handle_request(req):
                # 从请求头中提取 token 和 cookie
                headers = req.headers
                if "token" in headers and not STATE["token"]:
                    STATE["token"] = headers["token"]
                    push_log(f"成功提取 Token: {STATE['token'][:10]}...", "success")
                
                if "cookie" in headers and "JSESSIONID" in headers["cookie"] and not STATE["cookie"]:
                    STATE["cookie"] = headers["cookie"]
                    push_log("成功提取 Cookies", "success")

            # 由于 Playwright 的 response 事件中读取 json 可能会造成死锁，改为使用 JS Hook 拦截 XHR
            # 取消原来的 python 级拦截
            def handle_request(req):
                # 仅在 Python 层提取 Header
                try:
                    headers = req.headers
                    if "token" in headers and not STATE["token"]:
                        STATE["token"] = headers["token"]
                        push_log(f"成功提取 Token (来自 Header): {STATE['token'][:10]}...", "success")
                    
                    if "cookie" in headers and "JSESSIONID" in headers["cookie"] and not STATE["cookie"]:
                        STATE["cookie"] = headers["cookie"]
                        push_log("成功提取 Cookies (来自 Header)", "success")
                except:
                    pass

            context.on("request", handle_request)
            page.goto("https://jwxk.jnu.edu.cn")
            
            # 持续运行，直到集齐关键数据并抓取到课程，或者用户手动关闭浏览器
            check_counter = 0
            while True:
                try:
                    # 检查是否所有页面都关了
                    if len(context.pages) == 0 or all(p.is_closed() for p in context.pages):
                        break
                except:
                    break

                # 注入 JS 拦截器和变量提取
                for p in context.pages:
                    try:
                        # 注入 XHR Hook
                        p.evaluate("""
                            if (!window._xhrHooked) {
                                window._xhrHooked = true;
                                window._capturedResponses = [];
                                window._capturedPayloads = [];
                                
                                // --- XHR Hook ---
                                const origOpen = XMLHttpRequest.prototype.open;
                                const origSend = XMLHttpRequest.prototype.send;
                                
                                // --- Fetch Hook (防御性升级) ---
                                if (window.fetch) {
                                    const origFetch = window.fetch;
                                    window.fetch = function(input, init) {
                                        if (init && init.__isGrabber) {
                                            return origFetch.apply(this, arguments);
                                        }
                                        let url = (typeof input === 'string') ? input : (input && input.url) || '';
                                        let body = (init && init.body) ? String(init.body) : '';
                                        
                                        if (body && body.includes('studentCode')) {
                                            window._capturedPayloads.push(body);
                                        }
                                        
                                        const urlParams = new URLSearchParams(window.location.search);
                                        const token = urlParams.get('token');
                                        if (token && !window._jnuToken) {
                                            window._jnuToken = token;
                                        }

                                        return origFetch.apply(this, arguments).then(res => {
                                            if (url) {
                                                const clonedRes = res.clone();
                                                clonedRes.json().then(data => {
                                                    if (data.dataList || data.rows || (data.data && Array.isArray(data.data))) {
                                                        window._capturedResponses.push({
                                                            url: url,
                                                            text: JSON.stringify(data)
                                                        });
                                                    }
                                                }).catch(e => {});
                                            }
                                            return res;
                                        });
                                    };
                                }
                                
                                XMLHttpRequest.prototype.open = function() {
                                    this._url = arguments[1] || "";
                                    return origOpen.apply(this, arguments);
                                };
                                
                                XMLHttpRequest.prototype.send = function(body) {
                                    if (body && typeof body === 'string' && body.includes('studentCode')) {
                                        window._capturedPayloads.push(body);
                                    }
                                    
                                    // Extract token from request headers or URL if needed, but easiest is to grab from URL
                                    const urlParams = new URLSearchParams(window.location.search);
                                    const token = urlParams.get('token');
                                    if (token && !window._jnuToken) {
                                        window._jnuToken = token;
                                    }

                                    this.addEventListener('load', function() {
                                        if (this._url) {
                                            try {
                                                const resp = JSON.parse(this.responseText);
                                                if (resp.dataList || resp.rows || (resp.data && Array.isArray(resp.data))) {
                                                    window._capturedResponses.push({
                                                        url: this._url,
                                                        text: this.responseText
                                                    });
                                                }
                                            } catch(e) {}
                                        }
                                    });
                                    return origSend.apply(this, arguments);
                                };
                                if (!window._onlinePollStarted) {
                                    window._onlinePollStarted = true;
                                    setInterval(() => {
                                        fetch("/xsxkapp/sys/xsxkapp/publicinfo/onlineUsers.do?timestamp=" + Date.now(), {
                                            headers: {"X-Requested-With": "XMLHttpRequest"},
                                            __isGrabber: true
                                        }).then(r => r.json()).then(d => {
                                            if(d && d.data && d.data.onlineUsers !== undefined) {
                                                window._onlineUsersCount = d.data.onlineUsers;
                                            }
                                        }).catch(()=>{});
                                    }, 2000);
                                }
                            }
                        """)

                        # 处理捕获到的 Payload (提取 studentCode 等)
                        payloads = p.evaluate("window._capturedPayloads || []")
                        if payloads:
                            p.evaluate("window._capturedPayloads = []") # 清空
                            import re
                            for pl in payloads:
                                decoded = urllib.parse.unquote(pl)
                                m_stu = re.search(r'"studentCode"\s*:\s*"([^"]+)"', decoded)
                                if m_stu and not STATE["studentCode"]:
                                    STATE["studentCode"] = m_stu.group(1)
                                    push_log(f"成功提取 学号: {STATE['studentCode']}", "success")
                                    
                                m_campus = re.search(r'"campus"\s*:\s*"([^"]+)"', decoded)
                                if m_campus and m_campus.group(1):
                                    if STATE.get("campus") != m_campus.group(1):
                                        STATE["campus"] = m_campus.group(1)
                                        push_log(f"成功更新 真实校区代码: {STATE['campus']}", "success")
                                    
                                m_batch = re.search(r'"electiveBatchCode"\s*:\s*"([^"]+)"', decoded)
                                if m_batch:
                                    batch_code = m_batch.group(1)
                                    STATE["electiveBatchCode"] = batch_code
                                    
                                    if '"XGXK"' in decoded:
                                        if STATE.get("batch_XGXK") != batch_code:
                                            STATE["batch_XGXK"] = batch_code
                                            push_log(f"成功更新 通选课轮次批次码: {batch_code}", "success")
                                    elif '"FANKC"' in decoded or '"TJKC"' in decoded:
                                        if STATE.get("batch_PRO") != batch_code:
                                            STATE["batch_PRO"] = batch_code
                                            push_log(f"成功更新 专业课轮次批次码: {batch_code}", "success")

                        # 处理捕获到的 学分信息 (原生突破 iframe 抓取)
                        realMax = 0
                        realSel = 0
                        for f in p.frames:
                            try:
                                max_texts = f.evaluate('Array.from(document.querySelectorAll(".max-credit-value, .max-credit-value-fx")).map(el => el.textContent)')
                                for text in max_texts:
                                    import re
                                    m = re.search(r'[\d\.]+', text)
                                    if m and float(m.group(0)) > 0:
                                        realMax = max(realMax, float(m.group(0)))
                                
                                sel_texts = f.evaluate('Array.from(document.querySelectorAll(".selected-credit-value, .selected-credit-value-fx")).map(el => el.textContent)')
                                for text in sel_texts:
                                    import re
                                    m = re.search(r'[\d\.]+', text)
                                    if m and float(m.group(0)) >= 0:
                                        realSel = max(realSel, float(m.group(0)))
                            except Exception:
                                pass
                                
                        if realMax > 0:
                            STATE["max_credit"] = realMax
                        if realSel > 0 and not STATE.get("credits_locked", False):
                            STATE["selected_credit"] = realSel

                        # 处理捕获到的 Responses (提取课程列表)
                        responses = p.evaluate("window._capturedResponses || []")
                        if responses:
                            p.evaluate("window._capturedResponses = []") # 清空
                            new_count = 0
                            for resp_obj in responses:
                                if isinstance(resp_obj, str):
                                    resp_str = resp_obj
                                    resp_url = ""
                                else:
                                    resp_str = resp_obj.get("text", "")
                                    resp_url = resp_obj.get("url", "")
                                
                                # 智能判定课程类型
                                inferred_class_type = "FANKC"
                                is_qxkc = False
                                if "recommendCourse" in resp_url:
                                    inferred_class_type = "TJKC"
                                elif "programCourse" in resp_url:
                                    inferred_class_type = "FANKC"
                                elif "publicCourse" in resp_url:
                                    inferred_class_type = "QXKC"
                                    is_qxkc = True
                                elif "curriculavariable" in resp_url.lower() or "xgxk" in resp_url.lower():
                                    inferred_class_type = "XGXK"

                                try:
                                    body = json.loads(resp_str)
                                    courses = body.get("dataList", body.get("rows", body.get("data", [])))
                                    
                                    if "courseresult.do" in resp_url.lower() and isinstance(courses, list):
                                        try:
                                            total_cred = sum(float(str(c.get("credit", c.get("courseCredit", "0")))) for c in courses if isinstance(c, dict))
                                            if total_cred > 0:
                                                STATE["selected_credit"] = total_cred
                                        except Exception:
                                            pass
                                            
                                    if isinstance(courses, list):
                                        for c in courses:
                                            tc_list = c.get("tcList", [])
                                            if not isinstance(tc_list, list) or len(tc_list) == 0:
                                                tc_list = [c]
                                                
                                            for tc in tc_list:
                                                cid = str(tc.get("teachingClassID", tc.get("teachingClassId", c.get("teachingClassId", c.get("id", "")))))
                                                if not cid: continue
                                                
                                                # Check both c and tc for selected status
                                                def is_truthy(val):
                                                    return str(val).lower() in ["true", "1"]
                                                is_selected = is_truthy(c.get("selected")) or is_truthy(tc.get("selected")) or is_truthy(c.get("hasSelect")) or is_truthy(tc.get("hasSelect"))
                                                if "courseresult" in resp_url.lower() or "course_result" in resp_url.lower() or "teachingtime" in resp_url.lower():
                                                    is_selected = True
                                                    
                                                course_data = {
                                                    "id": cid,
                                                    "courseCode": str(c.get("courseNumber", c.get("courseCode", c.get("courseId", "")))),
                                                    "name": str(c.get("courseName", c.get("departmentName", "未知课程"))),
                                                    "teacher": str(tc.get("teacherName", tc.get("engTeacherNameList", c.get("engTeacherNameList", "未知")))),
                                                    "time": str(tc.get("teachingPlace", tc.get("classTime", c.get("classTime", "未知时间")))),
                                                    "credit": str(c.get("credit", c.get("courseCredit", "0"))),
                                                    "type": str(c.get("courseTypeName", c.get("typeName", c.get("courseNatureName", "未知")))),
                                                    "teachingClassType": inferred_class_type,
                                                    "selected": is_selected,
                                                    "isConflict": str(c.get("isConflict", tc.get("isConflict", "0"))),
                                                    "conflictDesc": str(c.get("conflictDesc", tc.get("conflictDesc", "")))
                                                }
                                                exist_c = next((x for x in STATE["captured_courses"] if x["id"] == course_data["id"]), None)
                                                if not exist_c:
                                                    # 拒绝自动将全校课程批量并入待抢列表，除非用户手动添加
                                                    if not is_qxkc:
                                                        STATE["captured_courses"].append(course_data)
                                                        new_count += 1
                                                else:
                                                    # 同步最新状态
                                                    if course_data["selected"] and not exist_c.get("selected", False):
                                                        exist_c["selected"] = True
                                                        # 如果引擎正在抢这门课，立刻宣布胜利
                                                        if STATE.get("is_grabbing") and any(t["id"] == exist_c["id"] for t in STATE["selected_targets"]):
                                                            push_log(f"🎉 [{exist_c['name']}] 后台状态同步：确认已选上！！！", "success")
                                                            push_log(f"[ACTION:SUCCESS_COURSE:{exist_c['id']}]", "info")
                                except ValueError:
                                    # 不是 JSON，可能是 HTML 页面
                                    import re
                                    # 去除 HTML 标签，提取纯文本
                                    text_only = re.sub(r'<[^>]+>', '', resp_str)
                                    text_only = re.sub(r'\s+', ' ', text_only).strip()
                                    
                                    # 检查是否包含常见的时间未到提示
                                    if "时间" in text_only or "未到" in text_only or "不在" in text_only or "开放" in text_only:
                                        push_log(f"⏳ 未到时间: {text_only[:80]}...", "warn")
                                    elif "登录" in text_only or "cas" in text_only.lower():
                                        push_log(f"💥 会话可能已过期，系统要求重新登录！", "error")
                                    else:
                                        push_log(f"💥 异常: 服务器未返回预期格式。", "error")
                            if new_count > 0:
                                push_log(f"成功通过底层 Hook 捕获到 {new_count} 门课程数据！", "success")

                        # 兜底 Cookie 提取
                        if not STATE["cookie"]:
                            cookies = context.cookies()
                            cookie_str = "; ".join([f"{c['name']}={c['value']}" for c in cookies])
                            if "JSESSIONID" in cookie_str:
                                STATE["cookie"] = cookie_str
                                push_log("成功提取 Cookies (从浏览器环境)", "success")
                                
                        # 轮询异步并发抢课的返回结果
                        async_res = p.evaluate("""
                            () => {
                                if (!window._asyncResponses || window._asyncResponses.length === 0) return null;
                                const res = window._asyncResponses;
                                window._asyncResponses = [];
                                return res;
                            }
                        """)
                        if async_res:
                            for item in async_res:
                                STATE["async_results_queue"].put(item)
                                
                        # 获取大盘人数
                        online_c = p.evaluate("window._onlineUsersCount")
                        if online_c is not None:
                            STATE["online_users_count"] = online_c

                    except Exception as e:
                        pass

                # 记录页面对象以供引擎发包
                if len(context.pages) > 0:
                    STATE["playwright_page"] = context.pages[0]

                # 不断尝试从拦截日志或者浏览器环境获取关键信息记录缺少的数据
                missing = []
                if not STATE["token"]: missing.append("Token")
                if not STATE["cookie"]: missing.append("Cookies")
                if not STATE["studentCode"]: missing.append("学号(studentCode)")
                if not STATE["electiveBatchCode"]: missing.append("选课批次码(electiveBatchCode)")
                if len(STATE["captured_courses"]) == 0: missing.append("课程列表(请点击选课分类)")

                # 自动模拟点击方案内与推荐班（仅在 Token 获取后且未曾点击时触发）
                if "auto_clicked_tabs" not in STATE:
                    STATE["auto_clicked_tabs"] = False

                if STATE["token"] and STATE["studentCode"] and not STATE["auto_clicked_tabs"]:
                    if len(STATE["captured_courses"]) == 0:
                        if "playwright_page" in STATE:
                            try:
                                js_script = """
                                    () => {
                                        if (window._autoClickerStarted) return;
                                        window._autoClickerStarted = true;
                                        
                                        const clickNode = (text) => {
                                            const els = Array.from(document.querySelectorAll('li, div, span, a, button'));
                                            const target = els.find(el => el.textContent && el.textContent.includes(text) && el.children.length === 0);
                                            if (target) {
                                                target.click();
                                                return true;
                                            }
                                            return false;
                                        };
                                        
                                        // 核心：依次模拟点击关键的三个按钮，强制前端发出请求，从而让后端拦截并提取轮次码(batch_PRO, batch_XGXK)
                                        const tabsToClick = [
                                            '切换轮次', '方案内课程', '推荐班课程', 
                                            '全校课程', '通识选修', '公共选修', 
                                            '跨专业课程', '方案外课程', '通识必修'
                                        ];
                                        let currentTabIndex = 0;
                                        let retries = 0;
                                        
                                        const interval = setInterval(() => {
                                            if (currentTabIndex >= tabsToClick.length) {
                                                clearInterval(interval);
                                                return;
                                            }
                                            let success = clickNode(tabsToClick[currentTabIndex]);
                                            if (success || retries >= 3) {
                                                currentTabIndex++;
                                                retries = 0;
                                            } else {
                                                retries++;
                                            }
                                        }, 1500);
                                        
                                        setTimeout(() => clearInterval(interval), 30000);
                                    }
                                """
                                STATE["playwright_page"].evaluate(js_script)
                                STATE["auto_clicked_tabs"] = True
                                push_log("🤖 自动为您模拟点击【切换轮次】、【方案内课程】等按钮，以获取关键轮次码", "info")
                            except Exception:
                                pass

                check_counter += 1
                if len(missing) > 0 and check_counter % 5 == 0:
                    push_log(f"⏳ 仍在等待提取: {', '.join(missing)}", "warn")

                # 如果集齐了所有参数
                if len(missing) == 0:
                    if not STATE["is_logged_in"]:
                        STATE["is_logged_in"] = True
                        push_log("✅ 所需参数及课程列表已全部捕获！请保持浏览器开启状态（可最小化），程序将通过浏览器底层通道发送请求！", "success")
                
                # 处理抢课指令
                try:
                    while not STATE["cmd_queue"].empty():
                        cmd = STATE["cmd_queue"].get_nowait()
                        if isinstance(cmd, tuple):
                            cmd_js, res_q = cmd
                            if "playwright_page" in STATE:
                                try:
                                    res = STATE["playwright_page"].evaluate(cmd_js)
                                    res_q.put(res)
                                except Exception as e:
                                    res_q.put(f"ERROR:{str(e)}")
                        else:
                            cmd_js = cmd
                            if "playwright_page" in STATE:
                                try:
                                    res = STATE["playwright_page"].evaluate(cmd_js)
                                    STATE["resp_queue"].put(res)
                                except Exception as e:
                                    STATE["resp_queue"].put(f"ERROR:{str(e)}")
                except Exception:
                    pass

                time.sleep(0.1)
    except Exception as e:
        push_log(f"Playwright 错误: {str(e)}", "error")

def send_elect_request_async_batch(ready_targets):
    js_code_lines = []
    js_code_lines.append("() => {")
    js_code_lines.append("    if (!window._asyncResponses) window._asyncResponses = [];")
    js_code_lines.append(f"    const concurrency = {STATE.get('concurrency', 1)};")
    js_code_lines.append("    const jnuToken = window._jnuToken || new URLSearchParams(window.location.search).get('token') || '';")
    
    for (target, att) in ready_targets:
        t_type = target.get("teachingClassType", "FANKC")
        batch_code = target.get("electiveBatchCode") or STATE["electiveBatchCode"]
        
        inner_data = {
            "operationType": "1",
            "studentCode": STATE["studentCode"],
            "electiveBatchCode": batch_code,
            "teachingClassId": target["id"],
            "isMajor": STATE["isMajor"],
            "campus": target.get("campus", STATE.get("campus", "2")),
            "teachingClassType": t_type,
        }
        
        if t_type == "XGXK" or t_type == "QXKC":
            inner_data["chooseVolunteer"] = "1"
            
        outer_data = {"data": inner_data}
        json_str = json.dumps(outer_data, ensure_ascii=False)
        encoded_data = urllib.parse.quote(json_str)
        payload = f"addParam={encoded_data}"
        
        js_code_lines.append(f"    // Target {target['name']}")
        js_code_lines.append("    for (let i = 0; i < Math.max(1, concurrency); i++) {")
        js_code_lines.append("        const ctrl = new AbortController();")
        js_code_lines.append("        const tid = setTimeout(() => ctrl.abort(), 8000);")
        js_code_lines.append(f"        fetch('{VOLUNTEER_URL}', {{")
        js_code_lines.append("            method: 'POST',")
        js_code_lines.append("            headers: {")
        js_code_lines.append("                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',")
        js_code_lines.append("                'X-Requested-With': 'XMLHttpRequest',")
        js_code_lines.append("                'token': jnuToken")
        js_code_lines.append("            },")
        js_code_lines.append(f"            body: '{payload}',")
        js_code_lines.append("            signal: ctrl.signal,")
        js_code_lines.append("            __isGrabber: true")
        js_code_lines.append("        }).then(r => {")
        js_code_lines.append("            clearTimeout(tid);")
        js_code_lines.append("            return r.text().then(body => {")
        js_code_lines.append("                window._asyncResponses.push({")
        js_code_lines.append(f"                    'id': '{target['id']}',")
        js_code_lines.append(f"                    'name': '{target['name']}',")
        js_code_lines.append(f"                    'att': {att},")
        js_code_lines.append("                    'status': r.status,")
        js_code_lines.append("                    'body': body")
        js_code_lines.append("                });")
        js_code_lines.append("            });")
        js_code_lines.append("        }).catch(e => {")
        js_code_lines.append("            window._asyncResponses.push({")
        js_code_lines.append(f"                'id': '{target['id']}',")
        js_code_lines.append(f"                'name': '{target['name']}',")
        js_code_lines.append(f"                'att': {att},")
        js_code_lines.append("                'status': 0,")
        js_code_lines.append("                'body': 'ERROR:' + e.message")
        js_code_lines.append("            });")
        js_code_lines.append("        });")
        js_code_lines.append("    }")
        
    js_code_lines.append("    return 'BATCH_DISPATCHED';")
    js_code_lines.append("}")
    
    js_code = "\n".join(js_code_lines)
    STATE["cmd_queue"].put(js_code)
    try:
        STATE["resp_queue"].get(timeout=2)
    except queue.Empty:
        pass

def send_elect_request_async(target, att):
    t_type = target.get("teachingClassType", "FANKC")
        
    # 如果目标课程自带了其对应的轮次批次码，优先使用它
    batch_code = target.get("electiveBatchCode") or STATE["electiveBatchCode"]
    
    inner_data = {
        "operationType": "1",
        "studentCode": STATE["studentCode"],
        "electiveBatchCode": batch_code,
        "teachingClassId": target["id"],
        "isMajor": STATE["isMajor"],
        "campus": target.get("campus", STATE.get("campus", "2")),
        "teachingClassType": t_type,
    }
    
    if t_type == "XGXK" or t_type == "QXKC":
        inner_data["chooseVolunteer"] = "1"

    
    # 根据真实的抓包逻辑，后端需要的参数名是 addParam，它的值是一个包含了 "data" 对象的完整 JSON 字符串。
    # 结构: addParam = {"data": {"operationType": "1", ...}}
    outer_data = {
        "data": inner_data
    }
    
    json_str = json.dumps(outer_data, ensure_ascii=False)
    encoded_data = urllib.parse.quote(json_str)
    payload = f"addParam={encoded_data}"
    
    js_code = f"""
    () => {{
        if (!window._asyncResponses) window._asyncResponses = [];
        const reqId = '{target['id']}';
        const jnuToken = window._jnuToken || new URLSearchParams(window.location.search).get('token') || '';
        
        const concurrency = {STATE.get("concurrency", 1)};
        
        for (let i = 0; i < Math.max(1, concurrency); i++) {{
            const ctrl = new AbortController();
            const tid = setTimeout(() => ctrl.abort(), 8000);
            
            fetch("{VOLUNTEER_URL}", {{
                method: "POST",
                headers: {{
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "X-Requested-With": "XMLHttpRequest",
                    "token": jnuToken
                }},
                body: '{payload}',
                signal: ctrl.signal,
                __isGrabber: true
            }}).then(r => {{
                clearTimeout(tid);
                return r.text().then(body => {{
                    window._asyncResponses.push({{
                        "id": reqId,
                        "name": "{target['name']}",
                        "att": {att},
                        "status": r.status,
                        "body": body
                    }});
                }});
            }}).catch(e => {{
                window._asyncResponses.push({{
                    "id": reqId,
                    "name": "{target['name']}",
                    "att": {att},
                    "status": 0,
                    "body": "ERROR:" + e.message
                }});
            }});
        }}
        return "DISPATCHED";
    }}
    """
    # 直接丢入命令队列，绝不阻塞等待返回！
    STATE["cmd_queue"].put(js_code)
    try:
        # 只等待 JS 执行完毕 (耗时不到1毫秒)，不等待 HTTP 响应
        STATE["resp_queue"].get(timeout=2)
    except queue.Empty:
        pass
def get_network_time_offset():
    try:
        # 使用淘宝高并发时间接口，并利用 requests.Session 复用底层 TCP 长连接
        res = time_session.get("http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp", timeout=2).json()
        tb_time = int(res["data"]["t"]) / 1000.0
        return tb_time - time.time()
    except Exception:
        return 0

def send_heartbeat():
    """通过浏览器发送一个轻量级请求来保持会话活跃"""
    js_code = f"""
    () => {{
        return fetch("{BASE_URL}/xsxkapp/sys/xsxkapp/elective/programCourse.do", {{
            method: "POST",
            headers: {{
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "X-Requested-With": "XMLHttpRequest"
            }},
            body: "data={{}}",
            __isGrabber: true
        }}).then(r => r.status).catch(() => 0);
    }}
    """
    STATE["cmd_queue"].put(js_code)
    STATE["cmd_queue"].put(js_code)
    try:
        for _ in range(50):
            if STATE.get("stop_event") and STATE["stop_event"].is_set():
                return
            try:
                result = STATE["resp_queue"].get(timeout=0.1)
                push_log(f"❤️ 心跳保活成功 (状态码: {result})", "info")
                return
            except queue.Empty:
                pass
        push_log("❤️ 心跳超时，但不影响运行", "warn")
    except Exception:
        pass

def try_silent_keepalive():
    """静默保活：定时拉取已选课表 (courseResult.do)，既维持 Session，又能将已选状态和学分同步给前端"""
    js_code = f"""
    () => {{
        const sc = "{STATE.get('studentCode', '')}";
        const batch = "{STATE.get('electiveBatchCode', '')}";
        const token = window._jnuToken || "{STATE.get('token', '')}";
        if (!sc || !batch || !token) return 0;
        
        const url = `{BASE_URL}/xsxkapp/sys/xsxkapp/elective/courseResult.do?timestamp=${{Date.now()}}&studentCode=${{sc}}&electiveBatchCode=${{batch}}`;
        return fetch(url, {{
            method: "GET",
            headers: {{
                "X-Requested-With": "XMLHttpRequest",
                "token": token
            }}
            // 不加 __isGrabber，故意让前端的钩子拦截到，从而同步到 Python 后端
        }}).then(r => r.status).catch(() => 0);
    }}
    """
    STATE["cmd_queue"].put(js_code)
    STATE["cmd_queue"].put(js_code)
    try:
        for _ in range(50):
            if STATE.get("stop_event") and STATE["stop_event"].is_set():
                return
            try:
                code = STATE["resp_queue"].get(timeout=0.1)
                if not STATE.get("is_grabbing"):
                    push_log(f"🛡️ 静默保活探针已发送 (HTTP {code})", "info")
                return
            except queue.Empty:
                pass
    except Exception:
        pass

def verify_course_state():
    """主动拉取一次课程列表，触发底层拦截器进行状态刷新"""
    try_silent_keepalive()

def grabbing_loop(targets, interval, schedule_time=0):
    try:
        _grabbing_loop_impl(targets, interval, schedule_time)
    except Exception as e:
        import traceback
        err_msg = traceback.format_exc()
        push_log(f"程序发生异常崩溃: {str(e)}", "error")
        print(err_msg)
    finally:
        STATE["is_grabbing"] = False
        push_log("抢课已停止", "warn")

def _grabbing_loop_impl(targets, interval, schedule_time=0):
    # 定时等待阶段
    if schedule_time > 0:
        offset = get_network_time_offset()
        now_net = time.time() + offset
        wait_seconds = schedule_time - now_net
        
        if wait_seconds > 0:
            target_str = datetime.fromtimestamp(schedule_time).strftime("%Y-%m-%d %H:%M:%S")
            push_log(f"⏰ 等待中，将在 {target_str} 开始抢课 (校准误差{offset*1000:.1f}ms)", "warn")
            push_log(f"自动保持登录状态中...", "info")
            last_heartbeat = 0
            
            while not STATE["stop_event"].is_set():
                current_net_time = time.time() + offset
                remain = schedule_time - current_net_time
                if remain <= 0:
                    break
                
                if remain > 2:
                    if time.time() - last_heartbeat > 30:
                        try:
                            try_silent_keepalive()
                            last_heartbeat = time.time()
                        except Exception:
                            pass
                    for _ in range(10):
                        if STATE["stop_event"].is_set(): break
                        time.sleep(0.1)
                elif remain > 0.1:
                    time.sleep(0.05)
                else:
                    time.sleep(0.002)
            
            if STATE["stop_event"].is_set():
                return
                
            push_log("时间到，开始发送请求！", "success")

    # 抢课主循环
    push_log(f"开始抢课，目标课程数: {len(targets)}，请求间隔: {interval}秒", "info")
    attempts = {t["id"]: 0 for t in targets}
    results = {t["id"]: False for t in targets}
    pending_reqs = {t["id"]: False for t in targets}
    last_fire_time = {t["id"]: 0 for t in targets}
    consecutive_errors = 0
    loop_count = 0

    # 清空残留异步结果
    while True:
        try:
            STATE["async_results_queue"].get_nowait()
        except queue.Empty:
            break

    while not STATE["stop_event"].is_set():
        all_done = all(results[t["id"]] for t in targets)
        if all_done:
            push_log("所有目标课程处理完毕", "success")
            break
            
        loop_count += 1
        
        # 每隔一段时间（约 5 秒）拉取一次底层状态库进行二次核验
        if loop_count % 50 == 0:
            verify_course_state()
            
        # 状态核验：在底层同步时如果已被选中，则立刻标记成功，不再发送请求
        for t in targets:
            if results[t["id"]]: continue
            exist_c = next((x for x in STATE["captured_courses"] if x["id"] == t["id"]), None)
            if exist_c and exist_c.get("selected", False):
                push_log(f"✅ [{t['name']}] 检查状态发现已选上！", "success")
                push_log(f"[ACTION:SUCCESS_COURSE:{t['id']}]", "info")
                results[t["id"]] = True

        # 如果在此刻已经全部成功，直接重新评估外层 while
        if all(results[t["id"]] for t in targets):
            continue

        # 收集就绪目标进行真并发批处理发包
        ready_targets = []
        for t in targets:
            if STATE["stop_event"].is_set(): break
            if results[t["id"]]: continue
            
            # [限制]: 如果该课程的上一发请求还没回来，不发第二发
            if pending_reqs[t["id"]]:
                # 超时断路器，防止网络丢包导致的永久等待
                if time.time() - last_fire_time[t["id"]] > 8.5:
                    pending_reqs[t["id"]] = False
                else:
                    continue
                    
            # [限制]: 独立控制每门课的请求间隔
            if time.time() - last_fire_time[t["id"]] < interval:
                continue

            # [限制]: 验证“选择”按钮是否亮起 (canSelect == "1")
            exist_c = next((x for x in STATE["captured_courses"] if x["id"] == t["id"]), None)
            current_can_select = exist_c.get("canSelect", "") if exist_c else str(t.get("canSelect", ""))
            if current_can_select and current_can_select != "1":
                continue
            
            attempts[t["id"]] += 1
            att = attempts[t["id"]]
            
            push_log(f"▶ [{t['name']}] 压入第 {att} 次全量并发队列...", "info")
                
            pending_reqs[t["id"]] = True
            last_fire_time[t["id"]] = time.time()
            ready_targets.append((t, att))

        if ready_targets:
            send_elect_request_async_batch(ready_targets)

        # 【处理上几轮积累的异步返回响应】
        while not STATE["stop_event"].is_set():
            try:
                res_item = STATE["async_results_queue"].get_nowait()
            except queue.Empty:
                break
            
            t_id = res_item["id"]
            name = res_item["name"]
            att = res_item["att"]
            
            # 接收到响应，解除等待状态，允许下一次请求
            if t_id in pending_reqs:
                pending_reqs[t_id] = False
            
            if results.get(t_id): continue
            
            http_status = res_item.get("status", 0)
            body_text = res_item.get("body", "")
            
            code = "-1"
            msg = "未知"
            if http_status == 200:
                try:
                    js_data = json.loads(body_text)
                    code = str(js_data.get("code", ""))
                    msg = str(js_data.get("msg", "未知响应"))
                except Exception:
                    import re
                    text_only = re.sub(r'<[^>]+>', '', body_text)
                    msg = str(re.sub(r'\s+', ' ', text_only).strip())
            
            if http_status in (500, 502, 503, 504):
                consecutive_errors += 1
                push_log(f"⚠️ [{name}] 第 {att} 次结果: HTTP {http_status} 服务器拥堵", "warn")
            elif http_status == 404:
                consecutive_errors += 1
                push_log(f"⚠️ [{name}] 第 {att} 次结果: HTTP 404 接口暂时不可用", "error")
            elif http_status == 0:
                consecutive_errors += 1
                push_log(f"⚠️ [{name}] 第 {att} 次结果: 网络超时或断开", "error")
            else:
                # HTTP 200 业务处理
                if code == "1" or "成功" in msg:
                    push_log(f"✅ [{name}] 第 {att} 次结果: 抢课成功！！！", "success")
                    push_log(f"[ACTION:SUCCESS_COURSE:{t_id}]", "info")
                    results[t_id] = True
                    consecutive_errors = 0
                    
                    try:
                        c_credit = float(next((t["credit"] for t in targets if t["id"] == t_id), 0))
                        STATE["selected_credit"] = STATE.get("selected_credit", 0) + c_credit
                        STATE["credits_locked"] = True # 锁定，防止前端还没刷新就被覆盖
                        import threading
                        threading.Timer(10.0, lambda: STATE.update({"credits_locked": False})).start()
                    except Exception:
                        pass
                elif code == "2":
                    consecutive_errors = 0
                    fatal = ["已选", "冲突", "不允许", "权限", "前置课程"]
                    if any(kw in msg for kw in fatal):
                        push_log(f"❌ [{name}] 第 {att} 次结果: {msg} (停止尝试)", "error")
                        results[t_id] = True
                    else:
                        push_log(f"❌ [{name}] 第 {att} 次结果: 被拒 {msg}", "error")
                else:
                    if "统一身份认证" in msg or "cas.jnu.edu.cn" in msg:
                        consecutive_errors += 1
                        push_log(f"⚠️ 登录可能失效，自动检查中...", "error")
                        try_silent_keepalive()
                    elif "时间" in msg or "未到" in msg or "不在" in msg or "开放" in msg:
                        consecutive_errors = 0
                        push_log(f"⏳ [{name}] 第 {att} 次结果: {msg[:50]}...", "warn")
                    elif "登录" in msg:
                        consecutive_errors += 1
                        push_log(f"⚠️ 登录异常，自动检查中...", "error")
                        try_silent_keepalive()
                    else:
                        consecutive_errors += 1
                        push_log(f"❌ [{name}] 第 {att} 次结果: 未知响应 {msg[:50]}", "error")

        # 全局退避
        if consecutive_errors >= 20:
            push_log(f"⚠️ 连续 {consecutive_errors} 次错误，暂停发送 5 秒...", "warn")
            time.sleep(5)
            consecutive_errors = 0
        elif consecutive_errors >= 8:
            time.sleep(1.5)
        else:
            time.sleep(0.1)

    STATE["is_grabbing"] = False
    push_log("抢课程序已停止", "warn")

# ==========================================
# 候补抢课引擎
# ==========================================
def waitlist_loop():
    push_log("候补轮询引擎已启动...", "info")
    while not STATE["waitlist_stop_event"].is_set():
        targets = list(STATE["waitlist_targets"].values())
        if not targets:
            time.sleep(1)
            continue
            
        for t in targets:
            if STATE["waitlist_stop_event"].is_set():
                break
                
            c_name = t.get("name", "")
            if not c_name:
                continue
                
            search_round = "XGXK" if t.get("uiTab") == "XGXK" else "PRO"
            batch_code = STATE.get("batch_XGXK") if search_round == "XGXK" else STATE.get("batch_PRO")
            if t.get("electiveBatchCode"):
                batch_code = t.get("electiveBatchCode")
                
            payload = {
                "data": {
                    "studentCode": STATE.get("studentCode", ""),
                    "campus": STATE.get("campus", "2"),
                    "electiveBatchCode": batch_code or STATE.get("electiveBatchCode", ""),
                    "isMajor": "1",
                    "teachingClassType": "QXKC",
                    "queryContent": c_name
                },
                "pageSize": "100",
                "pageNumber": "0",
                "order": ""
            }
            
            import urllib.parse
            json_str = json.dumps(payload, ensure_ascii=False)
            encoded_data = urllib.parse.quote(json_str)
            req_data = f"querySetting={encoded_data}"
            
            js_code = f"""
            () => {{
                return fetch("{BASE_URL}/xsxkapp/sys/xsxkapp/elective/publicCourse.do", {{
                    method: "POST",
                    headers: {{
                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "X-Requested-With": "XMLHttpRequest",
                        "token": window._jnuToken || "{STATE.get('token', '')}"
                    }},
                    body: "{req_data}",
                    __isGrabber: true
                }}).then(res => res.json()).catch(err => null);
            }}
            """
            
            res_q = queue.Queue()
            STATE["cmd_queue"].put((js_code, res_q))
            try:
                res = res_q.get(timeout=5)
                if res and str(res.get("code")) == "1":
                    data_list = res.get("dataList", [])
                    matched_course = next((c for c in data_list if str(c.get("teachingClassID")) == str(t["id"])), None)
                    if matched_course:
                        num_selected = int(matched_course.get("numberOfSelected", 0) or 0)
                        capacity = int(matched_course.get("classCapacity", 0) or 0)
                        can_select = str(matched_course.get("canSelect", "1"))
                        
                        if num_selected < capacity:
                            if can_select == "1":
                                push_log(f"🎉 [候补] 发现空缺且开放选择！[{t['name']}] 已选 {num_selected}/{capacity}，正在发起抢课并发请求！", "success")
                                send_elect_request_async(t, 1)
                            else:
                                # 发现空缺但按钮未亮起
                                pass
                        else:
                            # print(f"[{t['name']}] 容量满: {num_selected}/{capacity}")
                            pass
            except Exception as e:
                pass
                
            time.sleep(1) # 请求间隔，减轻服务器压力
            
        # 处理抢课结果队列 (处理可能由候补触发的响应)
        # 如果主抢课循环在运行，它也会帮忙处理
        while not STATE["waitlist_stop_event"].is_set():
            try:
                res_item = STATE["async_results_queue"].get_nowait()
                t_id = res_item["id"]
                name = res_item["name"]
                http_status = res_item.get("status", 0)
                body_text = res_item.get("body", "")
                
                code = "-1"
                msg = "未知"
                if http_status == 200:
                    try:
                        js_data = json.loads(body_text)
                        code = str(js_data.get("code", ""))
                        msg = str(js_data.get("msg", "未知响应"))
                    except Exception:
                        import re
                        text_only = re.sub(r'<[^>]+>', '', body_text)
                        msg = str(re.sub(r'\s+', ' ', text_only).strip())
                        
                if code == "1" or "成功" in msg:
                    push_log(f"✅ [{name}] 抢课成功！！！", "success")
                    push_log(f"[ACTION:SUCCESS_COURSE:{t_id}]", "info")
                    if t_id in STATE["waitlist_targets"]:
                        del STATE["waitlist_targets"][t_id]
                elif code == "2":
                    fatal = ["已选", "冲突", "不允许", "权限", "前置课程"]
                    if any(kw in msg for kw in fatal):
                        push_log(f"❌ [{name}] 结果: {msg} (不再尝试)", "error")
                        if t_id in STATE["waitlist_targets"]:
                            del STATE["waitlist_targets"][t_id]
                    else:
                        push_log(f"⚠️ [{name}] 被拒 {msg} (继续候补)", "warn")
                else:
                    push_log(f"⚠️ [{name}] 候补响应异常 {msg[:50]}", "warn")
            except queue.Empty:
                break
                
    push_log("候补轮询引擎已停止", "warn")

# ==========================================
# Flask 路由
# ==========================================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/status")
def api_status():
    return jsonify({
        "is_logged_in": STATE["is_logged_in"],
        "is_grabbing": STATE["is_grabbing"],
        "studentCode": STATE["studentCode"],
        "courses_count": len(STATE["captured_courses"]),
        "max_credit": STATE.get("max_credit", 0),
        "selected_credit": STATE.get("selected_credit", 0)
    })

@app.route("/api/online_users")
def get_online_users():
    val = STATE.get("online_users_count", "--")
    if val != "--":
        return jsonify({"success": True, "count": val})
    return jsonify({"success": False, "count": "--"})
@app.route("/api/login", methods=["POST"])
def api_login():
    if not STATE["is_logged_in"]:
        threading.Thread(target=run_playwright_login, daemon=True).start()
        return jsonify({"success": True, "msg": "正在唤起浏览器..."})
    return jsonify({"success": False, "msg": "已经登录过了"})

@app.route("/api/courses")
def api_courses():
    return jsonify({"success": True, "courses": STATE["captured_courses"]})

@app.route("/api/delete_course", methods=["POST"])
def api_delete_course():
    data = request.json
    cid = data.get("id")
    if cid:
        STATE["captured_courses"] = [c for c in STATE["captured_courses"] if c["id"] != cid]
        try:
            with open(get_data_path("targets.json"), "w", encoding="utf-8") as f:
                json.dump({
                    "courses": STATE["captured_courses"],
                    "selected": STATE["selected_targets"]
                }, f, ensure_ascii=False, indent=4)
            return jsonify({"success": True})
        except Exception as e:
            return jsonify({"success": False, "msg": str(e)})
    return jsonify({"success": True})

@app.route('/api/load_targets', methods=['GET'])
def load_targets():
    target_file = get_data_path("targets.json")
    if not os.path.exists(target_file):
        return jsonify({"success": True, "data": {"courses": [], "selected": []}})
    try:
        with open(target_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify({"success": True, "data": data})
    except Exception as e:
        return jsonify({"success": False, "msg": str(e)})

@app.route("/api/fetch_courses_active", methods=["POST"])
def api_fetch_courses_active():
    try:
        if not STATE.get("is_logged_in") or STATE.get("playwright_page") is None:
            return jsonify({"success": False, "msg": "未登录或浏览器未就绪"})
            
        data = request.json or {}
        course_type = data.get("courseType", "FANKC")
        query_content = data.get("queryContent", "")
        campus = data.get("campus", STATE.get("campus", "1"))
        search_round = data.get("searchRound", "AUTO")
        
        batch_code = STATE.get("electiveBatchCode", "")
        if search_round == "PRO" and STATE.get("batch_PRO"):
            batch_code = STATE["batch_PRO"]
        elif search_round == "XGXK" and STATE.get("batch_XGXK"):
            batch_code = STATE["batch_XGXK"]
        
        url_map = {
            "FANKC": "https://jwxk.jnu.edu.cn/xsxkapp/sys/xsxkapp/elective/programCourse.do",
            "TJKC": "https://jwxk.jnu.edu.cn/xsxkapp/sys/xsxkapp/elective/recommendCourse.do",
            "QXKC": "https://jwxk.jnu.edu.cn/xsxkapp/sys/xsxkapp/elective/publicCourse.do"
        }
        target_url = url_map.get(course_type)
        if not target_url:
            return jsonify({"success": False, "msg": "未知的课程类型"})
            
        payload = {
            "data": {
                "studentCode": STATE.get("studentCode", ""),
                "campus": str(campus),
                "electiveBatchCode": batch_code,
                "isMajor": "1",
                "teachingClassType": course_type,
                "queryContent": query_content
            },
            "pageSize": "100" if course_type == "QXKC" else "2000",
            "pageNumber": "0",
            "order": ""
        }
        
        import urllib.parse
        json_str = json.dumps(payload, ensure_ascii=False)
        encoded_data = urllib.parse.quote(json_str)
        req_data = f"querySetting={encoded_data}"
        
        js_code = f"""
        () => {{
            return fetch("{target_url}", {{
                method: "POST",
                headers: {{
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "X-Requested-With": "XMLHttpRequest",
                    "token": window._jnuToken || "{STATE.get('token', '')}"
                }},
                body: "{req_data}",
                __isGrabber: true
            }}).then(res => res.json()).catch(err => ({{ code: "-1", msg: err.toString() }}));
        }}
        """
        
        res_q = queue.Queue()
        STATE["cmd_queue"].put((js_code, res_q))
        
        try:
            res = res_q.get(timeout=10)
        except queue.Empty:
            return jsonify({"success": False, "msg": "请求浏览器执行超时"})
            
        if isinstance(res, str) and res.startswith("ERROR:"):
            return jsonify({"success": False, "msg": f"浏览器底层错误: {res[6:]}"})
        
        if res and str(res.get("code")) == "1":
            actual_round = "XGXK" if batch_code == STATE.get("batch_XGXK") and batch_code else "PRO"
            return jsonify({"success": True, "data": res.get("dataList", []), "courseType": course_type, "actualRound": actual_round})
        else:
            return jsonify({"success": False, "msg": res.get("msg", f"获取{course_type}失败")})
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"success": False, "msg": f"后端异常: {str(e)}"})

@app.route("/api/save_targets", methods=["POST"])
def api_save_targets():
    try:
        data = request.json
        with open("targets.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "msg": str(e)})

@app.route("/api/load_targets", methods=["GET"])
def api_load_targets():
    import os
    if not os.path.exists("targets.json"):
        return jsonify({"success": True, "data": []})
    try:
        with open("targets.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify({"success": True, "data": data})
    except Exception as e:
        return jsonify({"success": False, "msg": str(e)})

@app.route("/api/time_sync")
def api_time_sync():
    start_t = time.time()
    offset = get_network_time_offset()
    latency = (time.time() - start_t) / 2
    STATE["time_offset"] = offset
    return jsonify({
        "offset": offset,
        "latency_ms": round(latency * 1000, 1)
    })

@app.route("/api/start", methods=["POST"])
def api_start():
    if STATE["is_grabbing"]:
        return jsonify({"success": False, "msg": "抢课已经在运行了"})
    
    data = request.json
    selected_courses = data.get("selected_courses", [])
    interval = float(data.get("interval", 1.0))
    schedule_time = float(data.get("schedule_time", 0.0))
    concurrency = int(data.get("concurrency", 1))
    
    if not selected_courses:
        return jsonify({"success": False, "msg": "请先勾选目标课程"})
    
    STATE["selected_targets"] = selected_courses
    STATE["concurrency"] = concurrency
    STATE["is_grabbing"] = True
    STATE["stop_event"].clear()
    
    STATE["grab_thread"] = threading.Thread(target=grabbing_loop, args=(selected_courses, interval, schedule_time), daemon=True)
    STATE["grab_thread"].start()
    
    return jsonify({"success": True, "msg": "启动成功"})

@app.route("/api/stop", methods=["POST"])
def api_stop():
    if STATE["is_grabbing"]:
        STATE["stop_event"].set()
        return jsonify({"success": True, "msg": "正在停止..."})
    return jsonify({"success": False, "msg": "未运行"})

@app.route("/api/stream")
def api_stream():
    def event_stream():
        while True:
            # 获取队列中的日志，无日志则阻塞
            log = STATE["logs"].get()
            yield f"data: {json.dumps(log)}\n\n"
    return Response(event_stream(), mimetype="text/event-stream")


@app.route("/api/waitlist/toggle", methods=["POST"])
def api_waitlist_toggle():
    data = request.json
    course = data.get("course")
    if not course or not course.get("id"):
        return jsonify({"success": False, "msg": "参数错误"})
        
    cid = course["id"]
    if cid in STATE["waitlist_targets"]:
        del STATE["waitlist_targets"][cid]
        push_log(f"已取消 [{course.get('name')}] 的候补", "info")
        
        if len(STATE["waitlist_targets"]) == 0 and STATE["waitlist_thread"]:
            STATE["waitlist_stop_event"].set()
            STATE["waitlist_thread"] = None
        
        return jsonify({"success": True, "status": "removed"})
    else:
        STATE["waitlist_targets"][cid] = course
        push_log(f"已将 [{course.get('name')}] 加入候补队列", "success")
        
        if STATE["waitlist_thread"] is None or not STATE["waitlist_thread"].is_alive():
            STATE["waitlist_stop_event"].clear()
            STATE["waitlist_thread"] = threading.Thread(target=waitlist_loop, daemon=True)
            STATE["waitlist_thread"].start()
            
        return jsonify({"success": True, "status": "added"})

@app.route("/api/waitlist/status")
def api_waitlist_status():
    return jsonify({
        "success": True, 
        "waitlist_targets": list(STATE["waitlist_targets"].keys())
    })

if __name__ == "__main__":
    import threading
    import webbrowser
    import subprocess
    
    # 确保 templates 文件夹存在 (对于源码运行)
    if not os.path.exists('templates') and not hasattr(sys, '_MEIPASS'):
        os.makedirs('templates')
        
    print("="*50)
    print("JNU 抢课系统 GUI 服务正在启动...")
    print("="*50)
    
    # 寻找可用端口
    import socket
    port = 5000
    for p in range(5000, 5010):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', p)) != 0:
                port = p
                break

    print(f"即将在浏览器中打开主页 (http://127.0.0.1:{port}) ...")
    
    # 关闭 PyInstaller 启动画面
    try:
        import pyi_splash
        pyi_splash.close()
    except ImportError:
        pass
    
    # 延迟 1 秒打开浏览器
    threading.Timer(1.0, lambda: webbrowser.open(f"http://127.0.0.1:{port}")).start()
    
    app.run(port=port, debug=False)
