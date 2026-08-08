from contextlib import asynccontextmanager

from src.core.logger import setup_logger
from src.core.db_registry import db
from src.core.executor import executor
from src.core.startup_state import startup_state
from src.core.llm_registry import llm_registry


@asynccontextmanager
async def lifespan(app):
    setup_logger()

    db.init()
    startup_state.db_pool_ready = True

    llm_registry.init()

    executor.init()

    startup_state.app_started = True

    yield

    executor.shutdown()

    await llm_registry.close()

    db.dispose()
