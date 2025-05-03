from sqlmodel import Session
from app.models.equipe import Equipe

def criar_equipe(session: Session, equipe: Equipe):
    session.add(equipe)
    session.commit()
    session.refresh(equipe)
    return equipe

