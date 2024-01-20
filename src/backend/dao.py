from typing import List

from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy import func

from .models import Job


def get(session: Session, offset=0, limit=100) -> List[Job]:
    result = session.query(Job).offset(offset).limit(limit).all()
    return result


def group_count(session: Session, key: str) -> dict:
    valid_keys = ["city", "education"]
    if key not in valid_keys:
        return {}
    group_by_column = getattr(Job, key)
    result = (
        session.query(group_by_column, func.count(Job.id))
        .group_by(group_by_column)
        .all()
    )
    result = sorted(result, key=lambda x: x[1], reverse=True)
    return {item[0]: item[1] for item in result}


def filtered_select(session: Session, exist: str) -> list[Job]:
    result = session.query(Job).filter(Job.position.like(f"%{exist}%")).all()
    return result
