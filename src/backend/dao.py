from typing import List
from sqlalchemy.orm import Session
from .models import Job


def get(session: Session, offset=0, limit=100) -> List[Job]:
    result = session.query(Job).offset(offset).limit(limit).all()
    return result
