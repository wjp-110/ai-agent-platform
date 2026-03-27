from langgraph.graph import StateGraph, END

from app.agent.state import AgentState
from app.llm.deepseek_llm import get_llm

llm = get_llm()


async def llm_node(state: AgentState):

    messages = state["messages"]

    response = await llm.ainvoke(messages)

    return {
        "messages": [response]
    }


builder = StateGraph(AgentState)

builder.add_node("llm", llm_node)

builder.set_entry_point("llm")

builder.add_edge("llm", END)

graph = builder.compile()