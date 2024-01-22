from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from .config import DB_URL

engine = create_engine(
    url=DB_URL,
    pool_pre_ping=True,
    pool_size=0,
    pool_recycle=3600,
    echo=False,
)

session_factory = sessionmaker(bind=engine, autoflush=False, expire_on_commit=True)

ScopedSession = scoped_session(session_factory)

Base = declarative_base()
