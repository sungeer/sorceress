from fastmcp import FastMCP

from src.config import settings
from src.lifespan import server_lifespan
from src.tools import register_all


def create_mcp():
    mcp = FastMCP(
        name='mcp-servers',
        instructions='MCP 服务：通过标准 MCP 协议对外暴露工具能力',
        version=settings.version,
        lifespan=server_lifespan,
    )

    register_all(mcp)

    return mcp
