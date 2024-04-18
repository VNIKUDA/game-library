from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from db import models, crud, schemas
from db.database import SessionLocal, engine

# Створення бази даних
models.Base.metadata.create_all(bind=engine)

# Додаток
app = FastAPI()

# Залжність для бази даних
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# СТВОРЕНННЯ (POST запити)
@app.post("/developers/create")
async def create_developer(developer: schemas.DeveloperCreate, db: Session = Depends(get_db)):
    return crud.create_developer(db, developer)

@app.post("/genres/create")
async def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    return crud.create_genre(db, genre)

@app.post("/games/create")
async def create_game(developer_id: int, genre_id: int, game: schemas.GameCreate, db: Session = Depends(get_db)):
    return crud.create_game(db, developer_id, genre_id, game)

@app.post("/games/{game_id}/reviews/create")
async def create_game_review(game_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return crud.create_review(db, game_id, review)