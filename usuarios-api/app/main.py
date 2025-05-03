from fastapi import FastAPI
from app.core.database import engine
from sqlmodel import SQLModel
from app.api import equipe, usuario

app = FastAPI()

SQLModel.metadata.create_all(engine)

app.include_router(equipe.router)
app.include_router(usuario.router)