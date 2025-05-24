from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine  
from sqlalchemy.orm import sessionmaker, declarative_base              
from dotenv import load_dotenv                                         
import os                                                              

load_dotenv()  # Загружаем переменные окружения из файла .env

# Читаем строку подключения из .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Создаём асинхронный движок SQLAlchemy с поддержкой asyncpg
engine = create_async_engine(DATABASE_URL, echo=True)

# Создаём фабрику сессий, которые используются в каждом запросе
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Базовый класс для описания моделей (таблиц)
Base = declarative_base()

# Зависимость для получения сессии базы данных в эндпоинтах
async def get_db():
    async with SessionLocal() as session:
        yield session  # возвращаем сессию (аналог подключения к БД)
