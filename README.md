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

## 📦 下载即用 (推荐)

本工具已经打包为**独立软件**，无需配置 Python 环境，小白即可一键启动：

1. **下载程序**：在 Releases 页面下载最新的 `JNU_Course_Grabber.exe`。
2. **直接运行**：双击运行 `JNU_Course_Grabber.exe`。
   - 首次运行时，Windows 可能会弹出保护提示，点击“更多信息” -> “仍要运行”。
   - 程序将自动唤起你电脑自带的 Edge 浏览器，无需额外下载庞大的内核。
3. **开始抢课**：
   - 在弹出的浏览器中正常登录教务系统。
   - 在黑框和弹出的控制台网页中，勾选目标课程即可一键挂机！

## 🛠️ 源码构建与开发

如果你想自行编译修改源码：

1. **环境准备**：安装 Python 3.8+。
2. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```
3. **一键打包为 EXE**：
   双击根目录下的 `build.bat` 脚本，即可全自动生成单文件独立的 `dist/JNU_Course_Grabber.exe` 软件。
4. **源码运行**：
   直接执行 `python app.py`。

## ⚠️ 免责声明

1. 本工具仅供学习、研究自动化测试与浏览器底层注入技术使用，**严禁用于任何商业用途或恶意攻击教务系统**。
2. 选课高峰期系统压力巨大，请合理设置请求间隔，不要对教务系统服务器造成过大负担。
3. 因使用本工具而导致的任何选课失败、账号封禁等后果，由使用者自行承担，开发者概不负责。

---
*If you find this project helpful, please give it a ⭐️!*
