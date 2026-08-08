from pathlib import Path

from dotenv import load_dotenv

base_dir = Path(__file__).resolve().parent.parent.parent

# development
dotenv_path = base_dir / '.env'
if dotenv_path.exists():
    load_dotenv(dotenv_path)


class BaseConfig:
    version = '26.0808.0818'

    jwt_algorithm = 'HS256'  # 加密算法
    jwt_access_token_expire_minutes = 30  # 访问令牌有效期 30分钟
