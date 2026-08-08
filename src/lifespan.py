from fastmcp.server.lifespan import lifespan

from src.core.db_registry import db
from src.core.executor import executor
from src.core.logger import setup_logger


@lifespan
async def server_lifespan(server):
    setup_logger()

    db.init()

    executor.init()

    yield

    executor.shutdown()

    db.dispose()
