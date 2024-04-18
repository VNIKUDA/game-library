# Імпорт модулів
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Шлях до бази даних
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# Двигун (не перевіряти однакові процеси)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_threads": False}
)
# Локальна сесії без авто пітвердження та змивання 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 
Base = declarative_base()