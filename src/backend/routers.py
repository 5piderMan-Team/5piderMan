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
def get_jobs(city: str | None = "All", session: Session = Depends(get_session)):
    return services.get_jobs(city, session)


@router.get("/analyze/{item}", response_class=JSONResponse)
def get_analyze(item: str, session: Session = Depends(get_session)):
    return services.group_and_count(session, item)


@router.get("/position/{spec}", response_model=list[schemas.SimpleJobSchema])
def get_certain_position(session: Session = Depends(get_session), spec: str = "python"):
    return services.get_filtered_position(session, spec)
