from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_db_end_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    create_db_end_tables()
    yield
    # Shutdown
    print("shutting down")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World This is a Simple Setup of FastAPI"}
