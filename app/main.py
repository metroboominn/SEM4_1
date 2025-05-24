from fastapi import FastAPI                 
from app.db import Base, engine             
from app.routes import router               

# Создаём экземпляр FastAPI-приложения
app = FastAPI()

# Событие при старте сервера
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # создаёт таблицы в базе, если их нет

# Главная страница — тестовая
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Подключаем маршруты из routes.py
app.include_router(router)
