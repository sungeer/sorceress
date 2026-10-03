from fastmcp.server.lifespan import lifespan

from src.core.logger import setup_logger
from src.core.http_client import httpx


@lifespan
async def server_lifespan(server):
    setup_logger()

    httpx.init()

    yield

    await httpx.aclose()
