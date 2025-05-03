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