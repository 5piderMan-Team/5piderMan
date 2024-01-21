from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from .config import settings

db_url = f"{settings.db_type}+{settings.db_api}://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

engine = create_engine(
    url=db_url,
    pool_pre_ping=True,
    pool_size=0,
    pool_recycle=3600,
    echo=False,
)

session_factory = sessionmaker(bind=engine, autoflush=False, expire_on_commit=True)

ScopedSession = scoped_session(session_factory)

Base = declarative_base()
