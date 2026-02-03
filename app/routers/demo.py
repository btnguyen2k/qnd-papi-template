from fastapi import APIRouter, Depends, HTTPException
from ..schemas import demo

router = APIRouter(prefix="/demo", tags=["demo"])

@router.get("/", response_model=demo.DemoHelloResponse, response_model_exclude_none=True)
def demo_hello():
    return demo.DemoHelloResponse()
