from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .equipe import Equipe

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str
    cargo: str
    id_equipe: Optional[int] = Field(default=None, foreign_key="equipe.id")

    equipe: Optional["Equipe"] = Relationship(back_populates="usuarios")

