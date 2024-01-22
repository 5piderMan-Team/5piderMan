from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from . import db, models, routers
from .config import HOST, PORT

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
async def static_filter(request: Request, call_next):
    urlpath = request.url.path
    # 如果是 fastapi 相关的路由，直接返回
    if (
        urlpath.startswith("/api")
        or urlpath.startswith("/docs")
        or urlpath.startswith("/redoc")
        or urlpath == "/openapi.json"
    ):
        return await call_next(request)

    # 如果访问首页，返回 index.html
    if urlpath == "/":
        return FileResponse(staticdir.joinpath("index.html"))

    # 如果访问静态资源，返回静态资源
    if urlpath.startswith("/assets") or urlpath == "/vite.svg":
        return FileResponse(staticdir.joinpath("." + urlpath))

    # 其他情况，例如前端路由，返回 index.html
    return FileResponse(staticdir.joinpath("index.html"))


app.include_router(routers.router, prefix="/api")


def create_tables() -> None:
    # 父类 Base 根据所有继承他的子类创建表
    models.Base.metadata.create_all(db.engine)


def main() -> None:
    # create_tables()

    uvicorn.run("backend.main:app", host=HOST, port=PORT, reload=True)
