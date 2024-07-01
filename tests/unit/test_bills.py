from app.service.bills import upload_batch_bills_service, check_file_already_uploaded
from tests.fixtures import test_csv_file


def test_return_amount_created_bank_slips(test_csv_file):
    """
    @notice Tests the upload_batch_bills_service function to ensure it correctly processes an uploaded CSV file and returns the expected amount of created bank slips.
    @param test_csv_file The CSV file containing the payment receivables data for the test.
    @dev This test uploads a CSV file and verifies that the number of created bank slips is as expected.
    @return amount The number of created bank slips from the uploaded CSV file.
    """
    files = {"file": ("input.csv", test_csv_file, "text.csv")}
    amount = upload_batch_bills_service(files)

    assert amount == 10
