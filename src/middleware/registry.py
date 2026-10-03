from src.middleware.tracing import RunIdMiddleware

middleware = [
    RunIdMiddleware(),
]
