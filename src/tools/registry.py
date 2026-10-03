from src.tools import echo


def register_all(mcp):
    mcp.tool(echo.echo)
