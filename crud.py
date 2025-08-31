from sqlmodel import Session
from schemas import CreateHero
from models import  Hero


def create_hero (session: Session, hero_create:CreateHero):
    hero=Hero.model_validate(hero_create)
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero