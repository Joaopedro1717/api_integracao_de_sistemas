from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_session
from app.schemas.equipe import EquipeCreate, EquipeRead
from app.repositories.equipe_repo import criar_equipe, listar_equipes, buscar_equipe_por_id

router = APIRouter(prefix="/equipes", tags=["equipes"])

@router.post("/", response_model=EquipeRead, status_code=201)
def criar(equipe: EquipeCreate, db: Session = Depends(get_session)):
    return criar_equipe(db, equipe)

@router.get("/", response_model=list[EquipeRead])
def listar(db: Session = Depends(get_session)):
    return listar_equipes(db)

@router.get("/{equipe_id}", response_model=EquipeRead)
def obter_equipe(equipe_id: int, db: Session = Depends(get_session)):
    equipe = buscar_equipe_por_id(db, equipe_id)
    if equipe is None:
        return {"error": "Equipe não encontrada"}
    return equipe