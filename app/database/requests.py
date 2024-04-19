from app.database.models import async_session
from app.database.models import User, Indicators
from sqlalchemy import select, update, delete

async def set_user(tg_id):
    async with async_session() as session: # Асинхронный запуск и закрытие сессии
        user = await session.scalar(select(User).where(User.tg_id == tg_id)) # возвращает объект с полями
        
        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()
            
async def set_food_time(timer):
    async with async_session() as session:
        stmt = (
                update(Indicators).
                where(Indicators.id == 1).
                values(food=timer)
                )
        await session.commit()
        
     
        
                   