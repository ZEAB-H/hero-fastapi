from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_db_end_tables
from routes import hero

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    create_db_end_tables()
    yield
    # Shutdown
    print("shutting down")

app = FastAPI(lifespan=lifespan)

# @app.get("/")
# async def root():
#     return {"message": "Hello World This is a Simple Setup of FastAPI"}


app.include_router(hero.router)