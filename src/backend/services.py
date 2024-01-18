from sqlalchemy.orm import Session

from . import dao


def get_jobs(session: Session):
    return dao.get(session)


def group_and_count(session: Session, key: str):
    if key == "position":
        print("hehe")
        lang = ["python", "java", "c++", "go", "ruby"]
        return {item: dao.keyword_count(session, item) for item in lang}

    return dao.group_count(session, key)
