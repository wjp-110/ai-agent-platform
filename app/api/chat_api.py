from fastapi import APIRouter
from pydantic import BaseModel
from langchain_core.messages import HumanMessage

from app.agent.agent_graph import graph
from app.core import limiter

router = APIRouter()

class ChatRequest(BaseModel):

    message: str


@router.post("/chat")
@limiter.limit("10/minute")
async def chat(req: ChatRequest):

    result = await graph.ainvoke({
        "messages": [
            HumanMessage(content=req.message)
        ]
    })

    return result