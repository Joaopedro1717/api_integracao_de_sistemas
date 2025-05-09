from sqlmodel import SQLModel, create_engine, Session
from .config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)

def create_db_and_tables():
    from app.models.equipe import Equipe
    from app.models.usuario import Usuario
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session