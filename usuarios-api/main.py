import redis
from fastapi import FastAPI
from app.core.database import create_db_and_tables
from app.api import equipe, usuario

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"message": "API de usuários e equipes"}

app.include_router(equipe.router)
app.include_router(usuario.router)