from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.database.postgres import init_postgres, close_postgres
from src.routes.sensor_routes import sensor_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_postgres()
    yield
    await close_postgres()


app: FastAPI = FastAPI(lifespan=lifespan, title="FastAPI TimescaleDB Sensor Data API")
app.include_router(sensor_router)
