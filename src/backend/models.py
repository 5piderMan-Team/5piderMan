from sqlalchemy import Column, Integer, String
from .db import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    position = Column(String(128), index=True)
    city = Column(String(128), index=True)
    area = Column(String(128))
    salary = Column(String(128))
    tag = Column(String(128))
    education = Column(String(128))
    experience = Column(String(128))
    company_name = Column(String(128))
    industry = Column(String(128))
    financing_stage = Column(String(128))
    company_size = Column(String(128))
    welfare = Column(String(128))
