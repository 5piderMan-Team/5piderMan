import time

from fastapi import APIRouter, Depends
from fastapi.logger import logger
from sqlalchemy.orm import Session

from . import db, schemas, services


def cache(func):
    # 缓存
    cache = None
    # 缓存开始时间
    bg = time.time()

    def wrapper(*args, **kwargs):
        nonlocal cache
        nonlocal bg
        # 如果缓存不存在或者缓存时间超过 1 小时，重新获取
        if cache is None:
            cache = func(*args, **kwargs)
            bg = time.time()
        if time.time() - bg > 3600:
            cache = func(*args, **kwargs)
            bg = time.time()
        return cache

    return wrapper


# FastAPI Dependency
def get_session():
    # 获得一个 session
    session = db.ScopedSession()
    try:
        yield session
    finally:
        session.close()


router = APIRouter()


@router.get("/jobs", response_model=list[schemas.JobSchema])
async def get_jobs(city: str | None = None, session: Session = Depends(get_session)):
    return services.get_jobs(city, session)


@router.get("/jobs/search", response_model=list[schemas.JobSchema])
async def get_jobs_search(keyword: str, session: Session = Depends(get_session)):
    return services.job_search(keyword, session)


city_cached = cache(services.get_city_analysis)
education_cached = cache(services.get_education_analysis)
position_cached = cache(services.get_position_analysis)
language_cached = cache(services.get_language_analysis)
salary_cached = cache(services.get_salary_analysis)
company_cached = cache(services.get_company_analysis)
category_cached = cache(services.get_category_analysis)
experience_cached = cache(services.get_experience_analysis)


@router.get("/analyze/{item}", response_model=dict[str, int])
async def get_analyze(item: str, session: Session = Depends(get_session)):
    match item:
        case "city":
            return city_cached(session)
        case "education":
            return education_cached(session)
        case "position":
            return position_cached(session)
        case "language":
            return language_cached(session)
        case "salary":
            return salary_cached(session)
        case "company_name":
            return company_cached(session)
        case "category":
            return category_cached(session)
        case "experience":
            return experience_cached(session)
        case _:
            print("invalid path parameters")
            return {"error": 404}


@router.post("/gpt", response_model=str)
async def gpt(request: schemas.GPT_Input):
    logger.warn(request)
    return services.gpt(request.input)
