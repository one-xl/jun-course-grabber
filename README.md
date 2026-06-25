# JNU Course Grabber 🎓

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**JNU Course Grabber (暨南大学全自动抢课助手)** 是一款专为暨南大学学生打造的高效、稳定且完全隐蔽的抢课工具。本系统基于 Python + Playwright 构建，通过底层网络请求拦截与会话保活技术，实现无感知的抢课体验。

## 🌟 核心特性

- **🚀 零延迟高并发抢课**：绕过前端排队，利用原生 `fetch` API 在后台静默发送极速请求，毫秒级响应。
- **🛡️ 绝对隐蔽与防反噬设计**：
  - 首创内部探针隔离机制（`__isGrabber`），底层劫持 `window.fetch` 与 `XMLHttpRequest`，完美剥离人工操作与脚本请求，防止系统逻辑出现“自我反噬”。
  - 零副作用：发往学校网关的请求与官方一模一样，无任何多余请求头，最大程度规避 WAF 防火墙拦截。
- **🔄 智能轮次识别与批次码动态更新**：
  - 无论你是处于“专业课轮次 (FANKC)”还是“全校通选课轮次 (XGXK)”，系统都能动态、无感知地自动抓取并更新最新的 `electiveBatchCode`。
- **❤️ 智能心跳保活**：底层探针定时发送轻量级心跳请求（Silent Keepalive），长效维持选课系统的 Session，挂机一整晚也不掉线。
- **📊 可视化面板与动态学分统计**：直观好用的 Web 控制台（基于 `templates/index.html` 构建），即刻同步选课学分状态，自动跳转对应轮次界面。

## 📦 文件结构

```text
JNU_Course_Grabber/
├── app.py                     # 核心抢课与 Playwright 底层注入引擎
├── templates/
│   └── index.html             # 可视化抢课操作面板
├── requirements.txt           # Python 依赖清单
├── 抢课系统，启动！.bat         # Windows 一键启动脚本
├── 使用文档.md / .docx        # 详细的使用指引
└── 图片演示.docx              # 图文并茂的操作说明
```

## 🛠️ 安装与使用

1. **安装依赖**
   请确保您已安装 Python 3.8 或以上版本。然后在终端中执行：
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

2. **启动系统**
   - Windows 用户：直接双击 `抢课系统，启动！.bat`。
   - 其他用户：在终端中运行 `python app.py`。

3. **登录与配置**
   - 脚本会自动打开浏览器并进入选课系统。
   - 扫码或输入密码登录后，正常浏览到选课界面，系统会在后台自动捕获你的 `studentCode` 和 `electiveBatchCode`。
   - 在本工具的控制台中搜索课程、加入目标、点击“开始抢课”即可挂机！

## ⚠️ 免责声明

1. 本工具仅供学习、研究自动化测试与浏览器底层注入技术使用，**严禁用于任何商业用途或恶意攻击教务系统**。
2. 选课高峰期系统压力巨大，请合理设置请求间隔，不要对教务系统服务器造成过大负担。
3. 因使用本工具而导致的任何选课失败、账号封禁等后果，由使用者自行承担，开发者概不负责。

---
*If you find this project helpful, please give it a ⭐️!*
