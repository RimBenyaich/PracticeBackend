from datetime import datetime
import logging
from typing import Optional
from fastapi import APIRouter
from ..services import repos as repos_services

router = APIRouter()

logger = logging.getLogger(__name__)

@router.get("/repos")
async def getLanguagesInformation(date: Optional[datetime] = datetime.now()):
    return await repos_services.getLanguagesInformation(date)
