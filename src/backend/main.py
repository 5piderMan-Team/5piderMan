from pathlib import Path
from .config import settings
from fastapi import Depends, FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
from . import models, db, dao, schemas, routers
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse

app = FastAPI()
app.include_router(routers.router, prefix="/api")

staticdir = Path(__file__).parent.parent.parent.joinpath("web/dist")
app.mount("/assets", StaticFiles(directory=staticdir / "assets"), name="static")


@app.get("/", response_class=HTMLResponse)
def root():
    return FileResponse(staticdir / "index.html")


def create_tables() -> None:
    # 父类 Base 根据所有继承他的子类创建表
    models.Base.metadata.create_all(db.engine)


def main() -> None:
    create_tables()

    uvicorn.run("backend.main:app", host=settings.host, port=settings.port, reload=True)
