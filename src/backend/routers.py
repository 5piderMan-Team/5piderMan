from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
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


@router.get("/analyze/{item}")
def get_analyze(session: Session = Depends(get_session), item: str | None = None):
    return services.group_and_count(session, item)