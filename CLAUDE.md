# sorceress 项目规范

## 代码风格
- 字符串优先使用单引号 `'`，除非字符串本身包含单引号
- 禁止使用 `global` 关键字

## 选型纪律
- 涉及库的 API 选型时，先通读该项目中该模块的现有代码，不要只凭记忆给方案
- 用户质疑选型时，优先查官方文档，以文档为准

## 执行环境
- 执行 Python 代码：`.venv\Scripts\python.exe <脚本>`
- 安装依赖：`.venv\Scripts\pip.exe install <包>`
- 禁止使用裸的 `python` 或 `pip` 命令