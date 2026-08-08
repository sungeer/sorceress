# sorceress

基于 [FastMCP](https://gofastmcp.com) 的纯 MCP 服务脚手架：通过标准 MCP 协议（streamable-http）对外暴露工具能力，内置 MySQL 原生 SQL 查询工具与全链路日志追踪。

## 快速开始

### 环境要求

- Python 3.13
- MySQL 8.4（使用内置 `query` 工具时需要，其余功能不依赖）

### 安装

```bash
$ git clone git@github.com:sungeer/sorceress.git
$ cd sorceress
```

创建并激活虚拟环境，安装依赖：

```bash
$ python -m venv .venv           # Windows: .venv\Scripts\activate
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

### 配置

复制 `.env.example` 为 `.env`，按需修改：

```bash
$ cp .env.example .env
```

当前模板只提供 `development` 环境配置，必须在 `.env` 中设置：

```
CONFIG_NAME=development
```

（`src/config/__init__.py` 的默认值是 `production`，未设置会启动失败。）

### 启动

```bash
$ uvicorn server:app --host 0.0.0.0 --port 7788
```

服务端点：`http://127.0.0.1:7788/mcp`

### 验证

```bash
$ .venv\Scripts\python.exe tests\list_tools.py   # 列出全部工具
$ .venv\Scripts\python.exe tests\call_echo.py    # 调用 echo 工具
```

## 项目结构

```
sorceress/
├── server.py              # 入口（uvicorn server:app 加载）
├── gunicorn.conf.py       # 生产部署配置
├── .env.example           # 环境变量模板
├── src/
│   ├── main.py            # create_mcp / create_app：应用装配
│   ├── lifespan.py        # 服务生命周期（日志、连接池、线程池）
│   ├── config/            # 环境配置（development 等）
│   ├── core/              # 基础设施：DB 连接池、线程池、日志、链路 id
│   ├── middleware/        # ASGI 中间件（X-Request-ID 链路追踪）
│   ├── tools/             # MCP 工具定义与注册
│   └── utils/             # 通用工具（线程池转协程）
└── tests/                 # 冒烟测试脚本（列出工具、调用工具）
```

## 添加新工具

1. 在 `src/tools/` 下新建模块，定义 `async` 函数与 `description` 变量：

```python
# src/tools/example.py
async def example(text: str) -> str:
    """示例工具"""
    return text

description = '示例工具：原样返回输入'
```

2. 在 `src/tools/__init__.py` 的 `register_all` 中注册：

```python
mcp.tool(example.example, name='example', description=example.description)
```

工具名默认即函数名，显式 `name`/`description` 仅为声明清晰；不传时 fastmcp 自动取函数名与 docstring。

## 链路追踪

- 每个 HTTP 请求自动生成 16 位十六进制链路 id（`run_id`）
- 客户端可传 `X-Request-ID` 请求头复用上游链路 id，响应头会原样回写
- 所有业务日志（loguru）自动携带 `[run_id]`，格式：

```
2026-08-08 09:03:22 - INFO - [2efb08a5500945ec] module:function:line - message
```

代码中取当前链路 id：`from src.core.context import run_id_var; run_id_var.get()`。

## 部署

生产环境可参考 `gunicorn.conf.py`（默认 `/srv` 路径、8848 端口，按实际环境调整）：

```bash
$ gunicorn server:app -c gunicorn.conf.py
```

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
