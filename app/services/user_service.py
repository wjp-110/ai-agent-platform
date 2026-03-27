from sqlalchemy import select
from app.db.mysql import AsyncSessionLocal
from app.db.models import User


async def get_users():

    async with AsyncSessionLocal() as session:

        result = await session.execute(
            select(User)
        )

        users = result.scalars().all()

        return [
            {
                "id": u.id,
                "name": u.name,
                "email": u.email
            }
            for u in users
        ]