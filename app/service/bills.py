import pandas as pd
from fastapi import UploadFile
from logging import Logger
from sqlalchemy.ext.asyncio import AsyncSession

from app.utils import read_upload_file, get_logger, generate_hash_file

logger: Logger = get_logger()


async def upload_batch_bills_service(db_session: AsyncSession, file: UploadFile) -> int:
    logger.info(f"Starting Process for {file.filename}!")
    buffered_file = await read_upload_file(file)
    data = pd.read_csv(buffered_file)
    # TODO generate hash
    # TODO check if file already has upload
    # TODO import bank slips in db -> imported
    # TODO generate bank slip
    # TODO generate bank slips in db -> generated
    # TODO send bank slip
    # TODO send bank slips in db -> sent
    # TODO return amount bank slips processed
    return data.head(n=15).to_dict()


def check_file_already_uploaded(content: bytes) -> int:
    logger.info(f"Checking if that file already was uploaded!")
    try:
        hash = generate_hash_file(content)
        # TODO check in database if hash already exists
        return "exists"
    except Exception as e:
        logger.error(
            "Failed to check if that file already was uploaded. Error: %s", str(e)
        )
        raise
