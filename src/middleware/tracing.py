import uuid

from fastmcp.server.middleware import Middleware, MiddlewareContext


class RunIdMiddleware(Middleware):

    async def on_call_tool(self, context: MiddlewareContext, call_next):
        run_id = str(uuid.uuid4())

        # token = run_id_var.set(run_id)
        try:
            return await call_next(context)
        finally:
            pass
