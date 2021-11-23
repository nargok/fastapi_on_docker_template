import uvicorn
from fastapi import FastAPI
from api.routers import task

app = FastAPI()

app.include_router(task.router)

@app.get("/hello")
async def hello():
    return { "message": "hello, world" }


if __name__ == "__name__":
    uvicorn.run(app, host="0.0.0.0", port=8000)