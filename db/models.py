from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

# Клас розробника
class Developer(Base):
    __tablename__ = "developers"

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, index=True)

    games = relationship("Game", back_populates="developer")

# Клас гри
class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, index=True, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

    developer_id = Column(Integer, ForeignKey("developers.id"))
    genre_id = Column(Integer, ForeignKey("genres.id"))

    developer = relationship("Developer", back_populates="games")
    genre = relationship("Genre", back_populates="games")
    reviews = relationship("Review", back_populates="game")

# Клас жанру
class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, index=True)

    games = relationship("Game", back_populates="genre")

# Клас відгук
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, index=True, primary_key=True)
    user = Column(String, index=True)
    text = Column(String, index=True)

    game_id = Column(Integer, ForeignKey("games.id"))

    game = relationship("Game", back_populates="reviews")