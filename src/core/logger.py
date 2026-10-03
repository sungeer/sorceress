import logging
import sys
from logging.handlers import TimedRotatingFileHandler

from src import settings
from src.core.context import exec_id_var


class RequestContextFilter(logging.Filter):
    """把当前请求的 exec_id 盖到每条日志记录上"""

    def filter(self, record):
        record.exec_id = exec_id_var.get()
        return True


def setup_logger():
    root_logger = logging.getLogger()

    logging.addLevelName(logging.DEBUG, 'DBG')
    logging.addLevelName(logging.INFO, 'INF')
    logging.addLevelName(logging.WARNING, 'WRN')
    logging.addLevelName(logging.ERROR, 'ERR')
    logging.addLevelName(logging.CRITICAL, 'CRT')

    root_logger.setLevel(logging.INFO)

    # fastmcp log
    fastmcp_logger = logging.getLogger('fastmcp')
    fastmcp_logger.handlers.clear()
    fastmcp_logger.propagate = True

    fmt = (
        '%(asctime)s | %(levelname)s | %(exec_id)s | '
        '%(message)s (%(name)s:%(lineno)d)'
    )

    context_filter = RequestContextFilter()

    formatter = logging.Formatter(
        fmt=fmt,
        defaults={
            'exec_id': '-'
        }
    )

    if settings.ENVIRONMENT == 'development':
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        console_handler.addFilter(context_filter)
        root_logger.addHandler(console_handler)

    log_file = settings.LOG_DIR / 'sorceress.log'

    file_handler = TimedRotatingFileHandler(
        log_file,
        when='midnight',
        backupCount=3,
        encoding='utf-8'
    )

    file_handler.setFormatter(formatter)
    file_handler.addFilter(context_filter)
    root_logger.addHandler(file_handler)
