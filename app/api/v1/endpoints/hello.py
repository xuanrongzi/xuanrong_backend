import logging
from datetime import datetime
from fastapi import APIRouter
from app.schemas.hello import HelloResponse

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/", response_model=HelloResponse)
async def read_root():
    return HelloResponse(message="Hello World")

@router.get("/hello/{name}", response_model=HelloResponse)
async def read_item(name: str):
    timestamp = datetime.now().isoformat()
    logger.info(f"{timestamp}::Request received - name: {name}")
    return HelloResponse(message=f"Hello {name}")