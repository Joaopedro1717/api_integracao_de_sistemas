from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.database import get_session
from app.schemas.usuario import UsuarioCreate, UsuarioRead
from app.services.usuario_service import criar_usuario_service, buscar_usuario_por_nome_service

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.post("/", response_model=UsuarioRead, status_code=201)
def criar_usuario(usuario: UsuarioCreate, session: Session = Depends(get_session)):
    return criar_usuario_service(session, usuario)

@router.get("/{nome}", response_model=UsuarioRead)
def buscar_usuario(nome: str, session: Session = Depends(get_session)):
    usuario = buscar_usuario_por_nome_service(session, nome)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario



