from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_db_end_tables
from routes.hero import router as hero_router  # More explicit import

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    create_db_end_tables()
    yield
    # Shutdown
    print("shutting down")

app = FastAPI(lifespan=lifespan)

app.include_router(hero_router)

@app.get("/")
async def root():
    return {"message": "Hero API is running"}