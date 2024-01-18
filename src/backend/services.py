from sqlalchemy.orm import Session

from . import dao


def get_jobs(session: Session):
    return dao.get(session)
