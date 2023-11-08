from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Classe pour représenter un badge
class Badge(BaseModel):
    Id: int
    Nom: str
    More: str
    Type: str
    Nombre: int

# Une liste temporaire pour stocker les badges (simule une base de données)
badges_db = []

# Classe pour représenter un utilisateur
class User(BaseModel):
    username: str
    password: str

# Liste temporaire de comptes utilisateurs (pour la démonstration)
users_db = []

# Route racine
@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

# Route pour obtenir la liste de badges
@app.get("/badge", response_model=List[Badge])
async def get_badges():
    return badges_db

# Route pour créer un badge
@app.post("/badge", response_model=Badge)
async def create_badge(badge: Badge):
    badges_db.append(badge)
    return badge

# Route pour créer un utilisateur
@app.post("/user", response_model=User)
async def create_user(user: User):
    users_db.append(user)
    return user

# Route pour obtenir la liste d'utilisateurs (pour la démonstration uniquement)
@app.get("/user", response_model=List[User])
async def get_users():
    return users_db

# Route pour mettre à jour les informations d'un utilisateur (pour la démonstration uniquement)
@app.put("/user/{username}", response_model=User)
async def update_user(username: str, user: User):
    for existing_user in users_db:
        if existing_user.username == username:
            existing_user.username = user.username
            existing_user.password = user.password
            return existing_user
    return {"error": "Utilisateur non trouvé"}
