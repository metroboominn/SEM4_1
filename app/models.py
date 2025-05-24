from sqlalchemy import Column, Integer, String  
from app.db import Base                         

# Описание таблицы users
class User(Base):
    __tablename__ = "users"  # имя таблицы в базе данных

    id = Column(Integer, primary_key=True, index=True)  # первичный ключ
    name = Column(String, index=True)                   # имя пользователя
