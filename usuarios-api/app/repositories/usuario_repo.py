from sqlmodel import Session, select
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate

def criar_usuario(session: Session, usuario_create: UsuarioCreate):
    novo_usuario = Usuario(**usuario_create.dict())
    session.add(novo_usuario)
    session.commit()
    session.refresh(novo_usuario)
    return novo_usuario

def buscar_usuario_por_nome(session: Session, nome: str):
    statement = select(Usuario).where(Usuario.nome == nome)
    usuario = session.exec(statement).first()
    return usuario

def buscar_usuario_por_id(session: Session, id: int) -> Usuario | None:
    statement = select(Usuario).where(Usuario.id == id)
    return session.exec(statement).first()
