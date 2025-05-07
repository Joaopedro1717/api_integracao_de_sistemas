from sqlmodel import Session
from app.schemas.usuario import UsuarioCreate, UsuarioRead
from app.models.usuario import Usuario
from app.repositories.usuario_repo import criar_usuario, buscar_usuario_por_nome, buscar_usuario_por_id
from app.core.redis_client import redis_client
import json

def criar_usuario_service(session: Session, usuario_create: UsuarioCreate) -> UsuarioRead:
    usuario = criar_usuario(session, usuario_create)
    # Limpar cache após criação
    redis_client.delete(f"usuario:{usuario.nome}")
    return usuario

def buscar_usuario_por_nome_service(session: Session, nome: str) -> UsuarioRead | None:
    cache_key = f"usuario:{nome}"

    # Verifica se usuário está no cache
    if cached := redis_client.get(cache_key):
        return UsuarioRead(**json.loads(cached))
    
    usuario = buscar_usuario_por_nome(session, nome)
    if usuario:
        redis_client.set(cache_key, json.dumps(usuario.model_dump()))
    return buscar_usuario_por_nome(session, nome)

def buscar_usuario_por_id_service(session: Session, id: int) -> UsuarioRead | None:
    usuario = buscar_usuario_por_id(session, id)
    if usuario:
        redis_client.set(f"usuario:{id}", json.dumps(usuario.model_dump()))
    return usuario