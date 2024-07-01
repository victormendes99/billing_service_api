import pytest
from io import BytesIO, StringIO
from fastapi import UploadFile

from app.utils import read_upload_file
from tests.fixtures import test_csv_file


@pytest.mark.asyncio
async def test_read_upload_file(test_csv_file):
    """
    @notice Tests the read_upload_file function to ensure it correctly reads an uploaded file and returns a StringIO object.
    @param test_csv_file A bytes-like object representing the CSV file content for the test.
    @dev This test creates an UploadFile object from the provided CSV content, calls the read_upload_file function,
         and verifies that the output is a StringIO object with the expected content.
    @return None
    """
    # Create a BytesIO object from the test CSV content
    file = BytesIO(test_csv_file)
    # Create an UploadFile object with the BytesIO object
    upload_file = UploadFile(filename="input.csv", file=file)

    # Call the read_upload_file function
    data = await read_upload_file(upload_file)

    # Assert that the returned data is an instance of StringIO
    assert isinstance(data, StringIO), "Expected data to be an instance of StringIO"

    # Move to the start of the StringIO object to read its content
    data.seek(0)
    # Assert that the content of the StringIO object matches the original CSV content
    assert (
        data.read() == test_csv_file.decode()
    ), "The content of StringIO does not match the original CSV content"
