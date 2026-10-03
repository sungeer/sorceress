from fastmcp import FastMCP

from src import settings
from src.core.lifespan import server_lifespan
from src.middleware.registry import middleware
from src.tools.registry import register_all


def create_mcp():
    mcp = FastMCP(
        name='mcp-servers',
        instructions='MCP Service',
        version=settings.VERSION,
        lifespan=server_lifespan,
        middleware=middleware,
    )

    register_all(mcp)

    return mcp
