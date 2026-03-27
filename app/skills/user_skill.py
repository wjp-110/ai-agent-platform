from langchain.tools import tool
from app.services.user_service import get_users


@tool
async def query_users():

    """
    查询系统中的所有用户
    """

    users = await get_users()

    return str(users)