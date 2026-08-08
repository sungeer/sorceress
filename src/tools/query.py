from src.core.db_registry import db
from src.core.executor import executor
from src.utils.concurrency import run_in_threadpool

_READ_ONLY_PREFIXES = ('SELECT', 'SHOW', 'DESCRIBE', 'EXPLAIN')

description = '在 MySQL 上执行只读 SQL 查询（仅 SELECT / SHOW / DESCRIBE / EXPLAIN），返回结果行列表'


async def query(sql: str) -> list:
    """
    在 MySQL 上执行只读 SQL 查询

    - 仅支持 SELECT / SHOW / DESCRIBE / EXPLAIN 开头的语句
    - 返回结果行列表，每行是一个 dict（列名 -> 值）
    - 查询在独立线程池执行，不阻塞事件循环
    """
    stripped = sql.strip().upper()
    if not stripped.startswith(_READ_ONLY_PREFIXES):
        raise ValueError('仅支持只读查询: SELECT / SHOW / DESCRIBE / EXPLAIN')

    def run_sync():
        with db.connect() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    return await run_in_threadpool(executor.db, run_sync)
