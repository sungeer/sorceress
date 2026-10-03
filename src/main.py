from fastmcp import FastMCP

from src import settings
from src.core.lifespan import server_lifespan
from src.middleware.registry import middleware
from src.tools import register_all


def create_mcp():
    mcp = FastMCP(
        name='mcp-servers',
        instructions='MCP 服务：通过标准 MCP 协议对外暴露工具能力',
        version=settings.VERSION,
        lifespan=server_lifespan,
        middleware=middleware,
    )

    register_all(mcp)

    return mcp
