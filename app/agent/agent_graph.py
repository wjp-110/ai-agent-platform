from langchain_core.messages import ToolMessage, AIMessage, HumanMessage, SystemMessage
from langgraph.graph import StateGraph, END
import json

from app.agent.state import AgentState
from app.llm.deepseek_llm import get_llm
from app.skills.loader import load_skills

llm = get_llm()
tools = load_skills()

# 构建系统提示词，告诉 LLM 有哪些工具可用
system_prompt = """你是一个智能助手，可以使用以下工具来帮助用户：

可用工具：
{tools_info}

当你需要使用工具时，请在回复中使用以下 JSON 格式：
{{"tool": "工具名称", "args": {{参数}}}}

例如：
{{"tool": "query_users", "args": {{}}}}

如果你不需要使用工具，直接回答用户的问题即可。"""

tools_info = "\n".join([f"- {t.name}: {t.description}" for t in tools])
system_prompt = system_prompt.format(tools_info=tools_info)


async def llm_node(state: AgentState):
    messages = state["messages"]

    # 添加系统提示词（如果是第一条消息）
    if len(messages) == 1 and isinstance(messages[0], HumanMessage):
        messages = [SystemMessage(content=system_prompt)] + messages

    response = await llm.ainvoke(messages)

    return {
        "messages": [response]
    }


async def tool_node(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]

    # 尝试从 AI 回复中解析工具调用
    if hasattr(last_message, "content"):
        content = last_message.content

        try:
            # 尝试解析 JSON
            if "{" in content and "}" in content:
                # 提取 JSON 部分
                start = content.find("{")
                end = content.rfind("}") + 1
                json_str = content[start:end]

                tool_call = json.loads(json_str)

                if "tool" in tool_call and "args" in tool_call:
                    tool_name = tool_call["tool"]
                    args = tool_call["args"]

                    # 查找并执行工具
                    for tool in tools:
                        if tool.name == tool_name:
                            result = await tool.ainvoke(args)

                            # 将结果添加到消息历史
                            return {
                                "messages": [
                                    HumanMessage(content=f"工具 {tool_name} 执行结果：{result}")
                                ]
                            }
        except:
            pass

    return {}


builder = StateGraph(AgentState)

builder.add_node("llm", llm_node)
builder.add_node("tools", tool_node)

builder.set_entry_point("llm")


def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]

    # 检查是否包含工具调用
    if hasattr(last_message, "content"):
        content = last_message.content
        if "{" in content and '"tool"' in content:
            return "tools"

    return END


builder.add_conditional_edges("llm", should_continue)
builder.add_edge("tools", "llm")

graph = builder.compile()
