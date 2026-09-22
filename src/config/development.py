import os

from src.config.base import BaseConfig, base_dir


class DevelopmentConfig(BaseConfig):
    environment = 'development'

    # MySQL 配置 (from .env, with local dev fallbacks)
    db_host = os.getenv('DB_HOST', '127.0.0.1')
    db_port = int(os.getenv('DB_PORT', '3306'))
    db_user = os.getenv('DB_USER', 'root')
    db_passwd = os.getenv('DB_PASSWORD', '')
    db_name = os.getenv('DB_NAME', 'viper')