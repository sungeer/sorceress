from src.tools import echo


def register_all(mcp):
    mcp.tool(echo.echo, name='echo', description='原样返回输入文本，用于验证 MCP 链路是否打通')
