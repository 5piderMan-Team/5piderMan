import logging
from typing import List

from sqlalchemy import Column, func
from sqlalchemy.orm import Session

from .models import Job


def match_field(field: str) -> Column[str]:
    match field:
        case "city":
            return Job.city
        case "position":
            return Job.position
        case "education":
            return Job.education
        case "experience":
            return Job.experience
        case "company_name":
            return Job.company_name
        case "industry":
            return Job.industry
        case "financing_stage":
            return Job.financing_stage
        case "company_size":
            return Job.company_size
        case "welfare":
            return Job.welfare
        case _:
            logging.error("Invalid field name")
            return Job.city


def get(session: Session, offset=0, limit=100) -> List[Job]:
    result = session.query(Job).offset(offset).limit(limit).all()
    return result


def group_count(session: Session, key: str) -> dict[str, int]:
    valid_keys = ["city", "education"]
    if key not in valid_keys:
        return {}
    group_by_column = match_field(key)

    result = (
        session.query(group_by_column, func.count(Job.id))
        .group_by(group_by_column)
        .all()
    )
    result = sorted(result, key=lambda x: x[1], reverse=True)
    return {item[0]: item[1] for item in result}


# select : exist in the target column
def existed_select(
    session: Session, field: str = "city", exist: str = "成都", offset=0, limit=100
) -> list[Job]:
    tar_attr = match_field(field)

    result = (
        session.query(Job)
        .filter(tar_attr.like(f"%{exist}%"))
        .offset(offset)
        .limit(limit)
        .all()
    )
    return result


def filter_count(session: Session, field: str, exist: str) -> int:
    tar_attr = match_field(field)
    result = session.query(Job).filter(tar_attr.like(f"%{exist}%")).count()
    return result
