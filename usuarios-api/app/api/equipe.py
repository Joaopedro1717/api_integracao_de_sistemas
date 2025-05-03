from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.services.equipe import criar_equipe
from app.schemas.equipe import EquipeCreate, EquipeRead

router = APIRouter(prefix="/equipe", tags=["Equipes"])

router.post("/", response_model=EquipeRead, status_code=201)
def criar(equipe: EquipeCreate, session: Session = Depends(get_session)):
    return criar_equipe(session, equipe)