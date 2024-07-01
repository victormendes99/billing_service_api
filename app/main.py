from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status

from app.db.database import sessionmanager
from app.api.v1.router import api_router
from app.logging import setup_logging
from app.metadata import (
    API_CONTACT,
    API_DESCRIPTION,
    API_TITLE,
    API_VERSION,
    LOGGER_NAME,
)

logger = setup_logging(LOGGER_NAME)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Function that handles startup and shutdown events.
    To understand more, read https://fastapi.tiangolo.com/advanced/events/
    """
    yield
    if sessionmanager._engine is not None:
        # Close the DB connection
        await sessionmanager.close()


app = FastAPI(
    lifespan=lifespan,
    title=API_TITLE,
    version=API_VERSION,
    contact=API_CONTACT,
    description=API_DESCRIPTION,
)

app.include_router(api_router)


@app.get("/")
async def healthy():
    raise HTTPException(status_code=status.HTTP_200_OK, detail="ping pong")
