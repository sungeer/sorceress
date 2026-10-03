import logging
import time

from fastmcp.server.middleware import Middleware, MiddlewareContext

logger = logging.getLogger(__name__)

_MAX_ARGS_LEN = 500


def _one_line(text) -> str:
    """压掉换行，保证一条日志只占一行，否则按相邻关系还原会错位"""
    return ' '.join(str(text).split())


def _format_args(arguments) -> str:
    text = _one_line(repr(arguments))
    if len(text) > _MAX_ARGS_LEN:
        return text[:_MAX_ARGS_LEN] + '...(truncated)'
    return text


class CallLogMiddleware(Middleware):

    async def on_call_tool(self, context: MiddlewareContext, call_next):
        tool = getattr(context.message, 'name', '-')
        arguments = getattr(context.message, 'arguments', None) or {}

        logger.info('call_start tool=%s args=%s', tool, _format_args(arguments))

        start = time.perf_counter()
        try:
            result = await call_next(context)
        except Exception as exc:
            duration_ms = (time.perf_counter() - start) * 1000
            logger.warning(
                'call_end tool=%s status=error duration_ms=%.2f error=%s: %s',
                tool,
                duration_ms,
                type(exc).__name__,
                _one_line(exc),
            )
            raise

        duration_ms = (time.perf_counter() - start) * 1000
        logger.info('call_end tool=%s status=ok duration_ms=%.2f', tool, duration_ms)

        return result
