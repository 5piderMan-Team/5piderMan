from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from . import db, models, routers
from .config import settings

staticdir = Path(__file__).parent.parent.parent.joinpath("web/dist")
# 目前采用 src 目录结构，导致打包时静态文件路径和开发时不一致，暂时先这样处理。
if not staticdir.exists():
    staticdir = Path(__file__).parent.parent.joinpath("web/dist")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_static_filter(request: Request, call_next):
    if request.url.path.startswith("/api") or request.url.path.startswith("/docs"):
        return await call_next(request)
    if request.url.path == "/":
        return FileResponse(staticdir.joinpath("index.html"))

    return FileResponse(staticdir.joinpath("." + request.url.path))


app.include_router(routers.router, prefix="/api")


def create_tables() -> None:
    # 父类 Base 根据所有继承他的子类创建表
    models.Base.metadata.create_all(db.engine)


def main() -> None:
    # create_tables()

    uvicorn.run("backend.main:app", host=settings.host, port=settings.port, reload=True)
