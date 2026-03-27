# test_db.py
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine


async def test_connection():
    engine = create_async_engine(
        "mysql+aiomysql://root:Mysql%402026@localhost:3306/agent_db",
        echo=True
    )

    try:
        async with engine.connect() as conn:
            print("✅ 数据库连接成功！")
    except Exception as e:
        print(f"❌ 连接失败：{e}")
    finally:
        await engine.dispose()


asyncio.run(test_connection())
