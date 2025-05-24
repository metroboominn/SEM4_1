from fastapi import APIRouter, Depends                    
from sqlalchemy.ext.asyncio import AsyncSession             
from sqlalchemy.future import select                       
from app.models import User                                
from app.db import get_db                                  

# Создаём роутер, чтобы потом подключить к основному приложению
router = APIRouter()

# GET-запрос: получаем всех пользователей
@router.get("/users")
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))  # выполняем SELECT * FROM users
    return result.scalars().all()            # возвращаем список пользователей

# POST-запрос: добавляем пользователя с именем
@router.post("/users")
async def create_user(name: str, db: AsyncSession = Depends(get_db)):
    new_user = User(name=name)         # создаём объект пользователя
    db.add(new_user)                   # добавляем в сессию
    await db.commit()                  # сохраняем изменения
    await db.refresh(new_user)         # обновляем объект из базы
    return new_user                    # возвращаем созданного пользователя
