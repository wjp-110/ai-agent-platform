from fastapi import FastAPI
from slowapi.middleware import SlowAPIMiddleware

from app.api.chat_api import router
from app.core import limiter

app = FastAPI()
app.include_router(router)

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
