from sqlalchemy.orm import Session

from . import dao


def get_jobs(city_limit: str | None, session: Session):
    if city_limit == "全国":
        return dao.get(session)
    return dao.existed_select(session, "city", city_limit)


def group_and_count(session: Session, key: str):
    if key not in ["city", "education"]:
        return {}
    return dao.group_count(session, key)


def get_filtered_position(session: Session, spec: str):
    current_pos = ["python", "ruby", "java", "c++"]
    if spec not in current_pos:
        return []
    return dao.existed_select(session, "position", spec)
