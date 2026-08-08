from starlette.middleware import Middleware

from src.middleware import tracing

middleware = [
    Middleware(tracing.RunIdMiddleware),  # 最外层 最先执行
]
