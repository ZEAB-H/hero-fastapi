from fastapi import APIRouter, Depends
from schemas import  CreateHero
from typing import  Annotated
from database import get_session
from sqlmodel import Session

router = APIRouter()
SessionDep= Annotated[Session, Depends(get_session())]
@router.post("/", response_model=CreateHero)
def create(hero: CreateHero, session: SessionDep):
    pass
