from . import dao
from sqlalchemy.orm import Session


def get_jobs(session: Session):
    return dao.get(session)
