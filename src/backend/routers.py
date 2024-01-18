from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import db, schemas, services


# FastAPI Dependency
def get_session():
    session = db.ScopedSession()
    try:
        yield session
    finally:
        session.close()


router = APIRouter()


@router.get("/jobs", response_model=list[schemas.JobSchema])
def get_jobs(session: Session = Depends(get_session)):
    return services.get_jobs(session)
