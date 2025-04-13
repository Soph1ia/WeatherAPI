from typing import Annotated
from fastapi import Body, FastAPI, HTTPException
from router import main_router, database_router
from contextlib import asynccontextmanager
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for FastAPI.
    Initializes the database connection and creates tables if they do not exist.
    """
    print("Starting up...")
    try:
        database_router.init_database()
        yield
    except Exception as e:
        print(f"Error during startup: {e}")
        raise HTTPException(
            status_code=500, 
            detail="Internal server error: Unable to initialize the database.")
    finally:
        print("Shutting down...")
        
app = FastAPI(
    title="Weather Sensor API", 
    version="1.0",
    description="API for managing and retrieving weather sensor data.",
    lifespan=lifespan,
    docs_url="/docs",
    )
    

# add router
app.include_router(main_router.router, prefix="/weather", tags=["Weather"])


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)