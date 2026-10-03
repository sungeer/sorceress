import logging
import sys
from logging.handlers import TimedRotatingFileHandler

from src import settings


def setup_logger():
    root_logger = logging.getLogger()

    logging.addLevelName(logging.DEBUG, 'DBG')
    logging.addLevelName(logging.INFO, 'INF')
    logging.addLevelName(logging.WARNING, 'WRN')
    logging.addLevelName(logging.ERROR, 'ERR')
    logging.addLevelName(logging.CRITICAL, 'CRT')

    root_logger.setLevel(logging.INFO)

    # logging.getLogger('fastmcp').setLevel(logging.WARNING)

    fmt = '%(asctime)s | %(levelname)s | %(message)s (%(name)s:%(lineno)d)'
    datefmt = '%H:%M:%S'

    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)

    if settings.ENVIRONMENT == 'development':
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)

    log_file = settings.LOG_DIR / 'sorceress.log'

    file_handler = TimedRotatingFileHandler(
        log_file,
        when='midnight',
        backupCount=3,
        encoding='utf-8'
    )

    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)
