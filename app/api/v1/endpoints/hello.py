from fastapi import APIRouter
from app.schemas.hello import HelloResponse

router = APIRouter()

@router.get("/", response_model=HelloResponse)
async def read_root():
    return HelloResponse(message="Hello World")

@router.get("/hello/{name}", response_model=HelloResponse)
async def read_item(name: str):
    return HelloResponse(message=f"Hello {name}")