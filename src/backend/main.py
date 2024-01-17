from pathlib import Path
from .config import settings
from fastapi import Depends, FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
from . import models, db, dao, schemas
from sqlalchemy.orm import Session


# 父类 Base 根据所有继承他的子类创建表
models.Base.metadata.create_all(db.engine)

app = FastAPI()


# Dependency
def get_session():
    session = db.ScopedSession()
    try:
        yield session
    finally:
        session.close()


staticdir = Path(__file__).parent.parent.parent.joinpath("web/dist")
app.mount("/static", StaticFiles(directory=staticdir), name="static")
app.mount("/assets", StaticFiles(directory=staticdir / "assets"), name="assets")


@app.get("/")
async def root():
    return FileResponse(staticdir / "index.html")


@app.get("/api/jobs", response_model=list[schemas.JobSchema])
def get_jobs(session: Session = Depends(get_session)):
    return dao.get(session)


def main():
    uvicorn.run("backend.main:app", host=settings.host, port=settings.port, reload=True)
