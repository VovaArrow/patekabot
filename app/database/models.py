from sqlalchemy import BigInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3') #Создаем базу данных ассинхронную

async_session = async_sessionmaker(engine) #Создаем подключение к базе данных

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):   #Класс дочерний с помощью Base можно управлять всеми таблицами
    
    __tablename__ = 'users' # Название таблицы
    
    id: Mapped[int] = mapped_column(primary_key=True) # Колонки
    tg_id = mapped_column(BigInteger)
    
class Indicators(Base):
    __tablename__ = 'indicators'  
    
    id: Mapped[int] = mapped_column(primary_key=True) # Колонки
    food: Mapped[str] = mapped_column(String(20))
    poof: Mapped[str] = mapped_column(String(20))
    iodine: Mapped[int] = mapped_column()
    vita_D: Mapped[int] = mapped_column()  
    
async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # Функция создает базу данных со всеми классами  
    