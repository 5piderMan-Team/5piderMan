from sqlalchemy.orm import Session

from . import dao


def get_jobs(session: Session):
    return dao.get(session)


def group_and_count(session: Session, key: str):
    return dao.count(session, key)
