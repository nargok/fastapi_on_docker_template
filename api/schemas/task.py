from pydantic import BaseModel, Field

from typing import Optional

class Task(BaseModel):
    id: int
    title: Optional[str] = Field(None, example="clean up room")