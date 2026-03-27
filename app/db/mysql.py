from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


engine = create_async_engine(

    settings.MYSQL_URL,

    # 连接池大小
    pool_size=20,

    # 最大溢出连接
    max_overflow=30,

    # 连接回收
    pool_recycle=1800,

    # 连接检测
    pool_pre_ping=True,

    echo=False
)


AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)