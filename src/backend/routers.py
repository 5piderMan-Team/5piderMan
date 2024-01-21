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
async def get_jobs(city: str | None = None, session: Session = Depends(get_session)):
    return services.get_jobs(city, session)


@router.get("/analyze/{item}", response_model=dict[str, int])
async def get_analyze(item: str, session: Session = Depends(get_session)):
    match item:
        case "city" | "education":
            return services.group_and_count(session, item)
        case "position":
            return services.get_position_analysis(session)
        case "language":
            return services.get_language_analysis(session)
        case "salary":
            return services.get_salary_analysis(session)
        case _:
            return {"error": 404}