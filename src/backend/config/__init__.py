from pathlib import Path

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
