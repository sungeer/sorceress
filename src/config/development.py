import os

from src.config.base import BaseConfig, base_dir


class DevelopmentConfig(BaseConfig):
    environment = 'development'

    # MySQL 配置
    db_host = '127.0.0.1'
    db_port = 3306
    db_user = 'root'
    db_passwd = 'admin'
    db_name = 'viper'
