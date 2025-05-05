import json
from app.core.redis_client import redis_client
from sqlmodel import Session, select
from app.models.equipe import Equipe
from app.schemas.equipe import EquipeCreate, EquipeRead

def criar_equipe(db: Session, equipe: EquipeCreate) -> Equipe:
    nova_equipe = Equipe(nome=equipe.nome)
    db.add(nova_equipe)
    db.commit()
    db.refresh(nova_equipe)

    #invalida o cacho após inserção
    redis_client.delete("equipes")

    return nova_equipe

def listar_equipes(db: Session) -> list[EquipeRead]:
    #Verifica cache
    cache = redis_client.get("equipes")
    if cache:
        equipes_json = json.loads(cache)
        return [EquipeRead(**e) for e in equipes_json]
    
    #Busca no banco
    equipes = db.exec(select(Equipe)).all()
    equipes_data = [EquipeRead.model_validate(e, from_attributes=True).model_dump() for e in equipes]

    #Armanzena no redis por 60 segundos 
    redis_client.set("equipes", json.dumps(equipes_data), ex=60)

    return [EquipeRead(**e) for e in equipes_data]

def buscar_equipe_por_id(db: Session, equipe_id: int) -> EquipeRead | None:
    #Tenta buscar no cache
    cache_key = f"equipe_{equipe_id}"
    cache = redis_client.get(cache_key)

    if cache:
        print(f"cache hit {equipe_id}")
        equipe_data = json.loads(cache)
        return EquipeRead(**equipe_data)
    
    equipe = db.exec(select(Equipe).where(Equipe.id == equipe_id)).first()

    #Se não encontrar no cache, busca no banco
    equipe = db.exec(select(Equipe).where(Equipe.id == equipe_id)).first()
    if equipe:
        print(f"cache miss {equipe_id}")
        equipe_data = EquipeRead.model_validate(equipe, from_attributes=True).model_dump()
        redis_client.set(cache_key, json.dumps(equipe_data), ex=60)
        return equipe_data
    
    print(f"equipe não encontrada {equipe_id}")
    return None