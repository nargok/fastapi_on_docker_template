from fastapi import APIRouter
import api.schemas.task as task_schema

router = APIRouter()

@router.get("/tasks")
async def list_tasks():
    return [task_schema.Task(id=1, title="todo1")]
