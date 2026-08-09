from src.tools import echo, query


def register_all(mcp):
    mcp.tool(echo.echo)
    mcp.tool(query.query)
