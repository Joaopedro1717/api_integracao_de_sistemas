from pydantic import BaseModel

class EquipeCreate(BaseModel):
    nome: str

class EquipeRead(BaseModel):
    id: int
    nome: str

    