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

# Просто заглушка
@app.get("/")
async def index(db: Session = Depends(get_db)):
    return "This is index page"