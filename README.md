技术栈：

- Web：FastAPI（全 async）
- Agent：LangGraph
- LLM：DeepSeek
- DB：MySQL
- Cache：Redis
- ORM：SQLAlchemy

目标能力：

- 多用户 Agent
- Redis 记忆
- Skill 插件系统
- MySQL 工具调用
- Agent workflow
- RAG 扩展能力
- Docker 部署
- async 全链路

架构

                ┌───────────────┐
                │   Frontend    │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │   FastAPI     │
                │   Gateway     │
                └───────┬───────┘
                        │
                        ▼
                 Agent Service
                        │
                        ▼
               LangGraph Workflow
                        │
        ┌───────────────┼────────────────┐
        │               │                │
       LLM            Skills           Memory
        │               │                │      
    DeepSeek API       Tools           Redis
                        │
                        ▼
                       MySQL
   
项目目录：

    ai-agent-platform/
    
    ├── app
        │
        ├── api
        │   └── chat_api.py
        │
        ├── agent
        │   ├── agent_graph.py
        │   └── state.py
        │
        ├── llm
        │   └── deepseek_llm.py
        │
        ├── skills
        │   ├── loader.py
        │   ├── base.py
        │   └── user_skill.py
        │
        ├── services
        │   └── user_service.py
        │
        ├── db
        │   ├── mysql.py
        │   └── models.py
        │
        ├── memory
        │   └── redis_memory.py
        │
        ├── core
        │   ├── config.py
        │   └── logger.py
        │
        ├── tests
        │   └── test_agent.py
        │
        ├── docker
        │   ├── Dockerfile
        │   └── docker-compose.yml
    │
    ├── main.py
    ├── requirements.txt