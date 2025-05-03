from typing import Optional
from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nome: str

class UsuarioRead(BaseModel):
    id: int
    nome: str