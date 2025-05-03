from app.schemas.equipe import EquipeCreate
from app.models.equipe import Equipe
from app.repositories import equipe as equipe_repo
from sqlmodel import Session

def criar_equipe(session: Session, equipe_data: EquipeCreate):
    nova_equipe = Equipe(nome=equipe_data.nome)
    return equipe_repo.criar_equipe(session, nova_equipe)