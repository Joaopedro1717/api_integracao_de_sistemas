from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    cargo: str
    id_equipe: int

class UsuarioRead(BaseModel):
    id: int
    nome: str
    email: str
    cargo: str
    id_equipe: int

    model_config = {
        "from_attributes": True
    }
