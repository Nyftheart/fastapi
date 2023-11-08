from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

class Badge(BaseModel):
    Id: int = 1
    Nom: str = "Test"
    More: str = "Test More"
    Type: str = "Badge de test"
    Nombre: int = 1

@app.get("/badge", response_model=Badge)
async def get_badge():
    return Badge()