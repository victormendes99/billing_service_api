from fastapi import APIRouter, Depends, status
from logging import Logger

from app.utils import get_logger

router = APIRouter()
logger: Logger = get_logger()


@router.get("/login", status_code=status.HTTP_200_OK)
async def login():
    logger.info("infooo")
    logger.warning("warninggg")
    logger.debug("debuggg")
    logger.error("error")
    return "Suceeded!"
