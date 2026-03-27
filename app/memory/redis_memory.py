import redis.asyncio as redis
from app.core.config import settings


pool = redis.ConnectionPool.from_url(

    settings.REDIS_URL,

    max_connections=50,

    decode_responses=True
)


redis_client = redis.Redis(
    connection_pool=pool
)


async def save_memory(session_id, message):

    await redis_client.rpush(session_id, message)


async def get_memory(session_id):

    messages = await redis_client.lrange(session_id, 0, -1)

    return messages