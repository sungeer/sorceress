from src.middleware import tracing

middleware = [
    tracing.RunIdMiddleware(),
]
