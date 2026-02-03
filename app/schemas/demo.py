from pydantic import BaseModel
from typing import Optional

class DemoBaseResponse(BaseModel):
    status: int
    message: str
    data: Optional[any] = None

    model_config = {
        "arbitrary_types_allowed": True
    }

class DemoHelloResponse(DemoBaseResponse):
    status: int = 200
    message: str = "Hello, World!"
