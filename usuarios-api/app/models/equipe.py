from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .usuario import Usuario

class Equipe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str

    usuarios: List["Usuario"] = Relationship(back_populates="equipe")

