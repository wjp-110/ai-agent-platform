from langchain_openai import ChatOpenAI
from app.core.config import settings


def get_llm():

    llm = ChatOpenAI(
        model="deepseek-chat",
        openai_api_key=settings.DEEPSEEK_API_KEY,
        openai_api_base="https://api.deepseek.com",
        temperature=0
    )

    return llm