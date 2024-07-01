from fastapi.testclient import TestClient
from fastapi import status

from app.main import app
from tests.fixtures import test_csv_file

client = TestClient(app)


def test_returns_status_code_200_when_csv_is_uploaded(test_csv_file):
    """
    @notice Tests the endpoint for uploading a CSV file to ensure it returns a status code 200 upon successful upload.
    @param test_csv_file The CSV file containing the payment receivables data for the test.
    @dev This test posts a CSV file to the /bills/upload-batch-bills/ endpoint and verifies that the response status code is 200.
    @return status_code The HTTP status code returned by the endpoint.
    """
    files = {"file": ("input.csv", test_csv_file, "text.csv")}
    response = client.post("/bills/upload-batch-bills/", files=files)

    assert response.status_code == status.HTTP_200_OK


def test_check_uploaded_file():
    pass
    # TODO check_file_already_uploaded


def test_check_new_file():
    pass
    # TODO check_file_already_uploaded
