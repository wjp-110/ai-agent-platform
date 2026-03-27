from fastapi import APIRouter, Request
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, AIMessage

from app.agent.agent_graph import graph
from app.core.limiter import limiter

router = APIRouter()

class ChatRequest(BaseModel):

    message: str

class ChatResponse(BaseModel):

    reply: str


@router.post("/chat")
@limiter.limit("10/minute")
async def chat(request: Request,req: ChatRequest):

    result = await graph.ainvoke({
        "messages": [
            HumanMessage(content=req.message)
        ]
    })

    # 提取最后一条 AI 消息作为回复
    messages = result.get("messages", [])
    ai_reply = ""
    for msg in reversed(messages):
        if isinstance(msg, AIMessage):
            ai_reply = msg.content if hasattr(msg, "content") else str(msg)
            break

    return ChatResponse(reply=ai_reply)