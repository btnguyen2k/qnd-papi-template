from pydantic import BaseModel
from typing import Optional, Any

class DemoBaseResponse(BaseModel):
    status: int
    message: str
    data: Optional[Any] = None

    model_config = {
        "arbitrary_types_allowed": True
    }

class DemoHelloResponse(DemoBaseResponse):
    status: int = 200
    message: str = "Hello, World!"
