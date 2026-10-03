from src.middleware.tracing import CallLogMiddleware

middleware = [
    CallLogMiddleware(),
]
