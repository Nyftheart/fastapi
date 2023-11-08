from fastapi import FastAPI
from pydantic import BaseModel
from typing import List  # Importez List depuis typing

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

class Badge(BaseModel):
    Id: int
    Nom: str
    More: str
    Type: str
    Nombre: int

# Une liste temporaire pour stocker les badges (simule une base de données)
badges_db = []

@app.get("/badge", response_model=List[Badge])  # Utilisez List[Badge]
async def get_badges():
    return badges_db

@app.post("/badge", response_model=Badge)
async def create_badge(badge: Badge):
    # Ajouter le badge à la liste des badges
    badges_db.append(badge)
    return badge
