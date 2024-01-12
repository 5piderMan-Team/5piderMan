from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table

app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")

# database
# replace your username and password below
engine = create_engine('mysql+pymysql://username:password@url:port/dbname')
metadata = MetaData()


@app.get("/")
async def root():
    return FileResponse("./static/html/homepage.html")


@app.get("/api/chart/city")
async def query_city():
    with engine.connect() as conn:
        with conn.begin():
            metadata.create_all(conn)
        metadata.reflect(conn)
        t = Table('job', metadata, autoload=True)
        # right here get the whole table data
        result = conn.execute(t.select()).all()
    # start statistic
    city_data = {}
    for row in result:
        city = row[2]
        if city in city_data:
            city_data[city] += 1
        else:
            city_data[city] = 1
    # sort the dict here
    city_data = dict(sorted(city_data.items(), key=lambda x: x[1], reverse=True))
    return JSONResponse(content=city_data)
