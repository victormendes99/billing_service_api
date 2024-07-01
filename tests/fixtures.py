import os
import pytest


@pytest.fixture
def test_csv_file():
    """Fixture to provide the test CSV file."""

    file_path = os.path.join(os.getcwd(), "tests/mock/input.csv")

    with open(file_path, "rb") as f:
        file_content = f.read()

    return file_content
