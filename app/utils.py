from __future__ import annotations

import logging
import hashlib
from io import StringIO
from fastapi import UploadFile
from functools import lru_cache


from app.metadata import LOGGER_NAME


@lru_cache()
def get_logger() -> lru_cache[logging.Logger]:

    return logging.getLogger(LOGGER_NAME)


logger: logging.Logger = get_logger()


async def read_upload_file(file: UploadFile) -> StringIO:
    """
    @notice Reads the content of an uploaded file and returns it as a StringIO object.
    @param file The uploaded file to be read.
    @dev This function reads the content of the uploaded file asynchronously, decodes it to a UTF-8 string, and returns it as a StringIO object.
    @return A StringIO object containing the decoded content of the uploaded file.
    @custom:warning If the file cannot be read, an error is logged and a ValueError is raised.
    """
    logger.info("Reading upload file")
    try:
        content = await file.read()
        return StringIO(content.decode("utf-8"))
    except Exception as e:
        logger.error("Failed to read the upload file. Error: %s", str(e))
        raise ValueError("Failed to read the upload file. Please try again.") from e


def generate_hash_file(content: bytes) -> str:
    """
    @notice Generates an MD5 hash digest for the provided byte content.
    @param content The byte content for which the hash needs to be generated.
    @dev This function computes the MD5 hash digest of the input byte content and returns it as a hexadecimal string.
    @return str The MD5 hash digest of the input content as a hexadecimal string.
    """
    try:
        md5_hash = hashlib.md5()
        md5_hash.update(content)
        return md5_hash.hexdigest()
    except Exception as e:
        logger.error("Failed to generate MD5 hash. Error: %s", str(e))
        raise
