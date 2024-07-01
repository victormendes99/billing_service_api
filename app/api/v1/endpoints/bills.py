from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status
from logging import Logger

from app.api.dependencies.database import DBSessionDep
from app.service.bills import upload_batch_bills_service
from app.utils import get_logger

router = APIRouter()
logger: Logger = get_logger()


@router.post("/upload-batch-bills/", status_code=status.HTTP_200_OK)
async def upload_batch_bills(db_session: DBSessionDep, file: UploadFile = File(...)):
    """
    @notice Endpoint for uploading a batch of bills as a CSV file.
    @param file The uploaded CSV file containing the batch of bills.
    @dev This endpoint receives an uploaded CSV file, processes it using the upload_batch_bills_service, and returns the result.
    @return A JSON response with the result of the batch bills processing.
    @custom:warning If the file processing fails, a HTTP 400 error is raised.
    """
    try:
        return await upload_batch_bills_service(file)
    except Exception as e:
        logger.error("Failed to process the upload file. Error: %s", str(e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to process the upload file. Please try again.",
        ) from e
