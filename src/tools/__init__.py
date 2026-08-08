from src.tools import echo, query


def register_all(mcp):
    mcp.tool(echo.echo, name='echo', description=echo.description)
    mcp.tool(query.query, name='query', description=query.description)
