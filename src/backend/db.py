from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from .config import settings

database_url = f"{settings.db_type}+{settings.db_api}://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

engine = create_engine(
    url=database_url,
    echo=True,
)

session_factory = sessionmaker(bind=engine, autoflush=False, expire_on_commit=True)

ScopedSession = scoped_session(session_factory)

Base = declarative_base()
