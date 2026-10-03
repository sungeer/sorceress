import logging
import time

from fastmcp.server.middleware import Middleware, MiddlewareContext

from src.core.context import exec_id_var
from src.utils.request_id import new_request_id

logger = logging.getLogger(__name__)


class CallLogMiddleware(Middleware):

    async def on_request(self, context: MiddlewareContext, call_next):
        token = exec_id_var.set(new_request_id())
        try:
            return await call_next(context)
        finally:
            exec_id_var.reset(token)

    async def on_call_tool(self, context: MiddlewareContext, call_next):
        tool = getattr(context.message, 'name', '-')

        start = time.perf_counter()
        try:
            result = await call_next(context)
        except Exception:
            logger.exception('call_error tool=%s', tool)
            raise
        finally:
            duration_ms = (time.perf_counter() - start) * 1000
            logger.info(
                'call_done tool=%s duration_ms=%.2f',
                tool, duration_ms
            )

        return result
