from sqlalchemy.orm import Session
from . import models, schemas


# СТВОРЕННЯ
def create_developer(db: Session, developer: schemas.DeveloperCreate):
    developer = models.Developer(name=developer.name)

    db.add(developer)
    db.commit()
    db.refresh(developer)

    return developer

def create_genre(db: Session, genre: schemas.GenreCreate):
    genre = models.Genre(name=genre.name)

    db.add(genre)
    db.commit()
    db.refresh(genre)

    return genre

def create_game(db: Session, developer_id, genre_id, game: schemas.GameCreate):
    game = models.Game(title=game.title, description=game.description, developer_id=developer_id, genre_id=genre_id)

    db.add(game)
    db.commit()
    db.refresh(game)

    return game

def create_review(db: Session, game_id: int, review: schemas.ReviewCreate):
    review = models.Review(user = review.user, text=review.text, game_id=game_id)

    db.add(review)
    db.commit()
    db.refresh(review)

    return review

