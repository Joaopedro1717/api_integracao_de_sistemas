from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_session
from app.schemas.equipe import EquipeCreate, EquipeRead
from app.repositories.equipe_repo import criar_equipe, listar_equipes

router = APIRouter(prefix="/equipes", tags=["equipes"])

@router.post("/", response_model=EquipeRead, status_code=201)
def criar(equipe: EquipeCreate, db: Session = Depends(get_session)):
    return criar_equipe(db, equipe)

@router.get("/", response_model=list[EquipeRead])
def listar(db: Session = Depends(get_session)):
    return listar_equipes(db)
