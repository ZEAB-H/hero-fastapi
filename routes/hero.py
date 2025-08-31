from fastapi import APIRouter, Depends
from schemas import CreateHero
from typing_extensions import Annotated  # Changed this line
from database import get_session
from sqlmodel import Session
import crud

router = APIRouter(prefix="/heros", tags=["hero"])
SessionDep = Annotated[Session, Depends(get_session)]

@router.post("/", response_model=CreateHero)
def create(hero: CreateHero, session: SessionDep):
    return crud.create_hero(session, hero)