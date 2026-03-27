from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

    MYSQL_URL = os.getenv(
        "MYSQL_URL",
        "mysql+aiomysql://root:123456@localhost:3306/agent_db"
    )

    REDIS_URL = os.getenv(
        "REDIS_URL",
        "redis://localhost:6379/0"
    )

settings = Settings()