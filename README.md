# sorceress

基于 [FastMCP](https://gofastmcp.com) 的纯 MCP 服务脚手架：通过标准 MCP 协议（streamable-http）对外暴露工具能力，内置 MySQL 原生 SQL 查询工具与全链路日志追踪。

## 快速开始

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

### 启动

```bash
$ fastmcp run server.py --transport http --host 0.0.0.0 --port 8848
```

服务端点：`http://127.0.0.1:7788/mcp`

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
