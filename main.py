from typing import Annotated

from fastapi import Body, FastAPI
from router import main_router

app = FastAPI(
    title="Weather Sensor API", 
    version="1.0",
    description="API for managing and retrieving weather sensor data."
    )

# add router
app.include_router(main_router.router, prefix="/weather", tags=["Weather"])