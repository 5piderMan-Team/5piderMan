from pathlib import Path
from typing import Any

from dynaconf import Dynaconf

configdir = Path(__file__).parent
settings_files = [
    Path.home() / ".config/backend/settings.toml",
    configdir / "settings.toml",
    configdir / ".secrets.toml",
]

settings = Dynaconf(
    envvar_prefix="5PIDERMAN",  # 环境变量前缀
    settings_files=settings_files,  # 配置文件
    load_dotenv=True,  # 加载 .env 文件
)


def try_to_load_str(key: str) -> str:
    res = None
    try:
        res = settings.__getattr__(key)
    except Exception:
        raise Exception(f"配置文件中缺少 {key} 字段")
    return res


def try_to_load_int(key: str) -> int:
    res = None
    try:
        res = settings.__getattr__(key)
    except Exception:
        raise Exception(f"配置文件中缺少 {key} 字段")
    return res


def load(key: str, default: Any = None) -> Any:
    res = None
    try:
        res = settings.__getattr__(key)
    except Exception:
        pass
        return default
    return res


# OpenAI API Key
OPENAI_API_KEY = load("OPENAI_API_KEY")
OPENAI_HOST = load("OPENAI_HOST")
# 数据库连接字符串
DB_TYPE = try_to_load_str("DB_TYPE")
DB_API = try_to_load_str("DB_API")
DB_USER = try_to_load_str("DB_USER")
DB_PASSWORD = try_to_load_str("DB_PASSWORD")
DB_HOST = try_to_load_str("DB_HOST")
DB_PORT = try_to_load_str("DB_PORT")
DB_NAME = try_to_load_str("DB_NAME")
DB_URL = f"{DB_TYPE}+{DB_API}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# 监听地址
HOST = load("HOST", "0.0.0.0")
# 监听端口
PORT = load("PORT", 8080)
