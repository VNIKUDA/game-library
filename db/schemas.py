from pydantic import BaseModel, Field
from typing import Annotated

class DeveloperBase(BaseModel):
    name: Annotated[str, Field(min_length=4, max_length=20)]

class DeveloperCreate(DeveloperBase):
    pass

class Developer(DeveloperBase):
    id: int
    games: list = []

    class Config:
        from_attributes = True


class GameBase(BaseModel):
    title: Annotated[str, Field(min_length=4, max_length=30)]
    description: Annotated[str, Field(min_length=4, max_length=300)]

class GameCreate(GameBase):
    pass

class Game(GameBase):
    id: int
    developer_id: int
    genre_id: int

    class Config:
        from_attributes = True


class GenreBase(BaseModel):
    name: Annotated[str, Field(min_length=4, max_length=20)]

class GenreCreate(GenreBase):
    pass

class Genre(GenreBase):
    id: int
    games: list = []

    class Config:
        from_attributes = True


class ReviewBase(BaseModel):
    user: Annotated[str, Field(min_length=4, max_length=20)]
    text: Annotated[str, Field(min_length=4, max_length=100)]

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    game_id: int

    class Config:
        from_attributes = True