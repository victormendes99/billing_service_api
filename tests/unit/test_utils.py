import hashlib

from app.utils import generate_hash_file
from tests.fixtures import test_csv_file


def test_generate_hash_file(test_csv_file: bytes):
    """
    @notice Tests the generate_hash_file function to ensure it correctly computes the MD5 hash for the provided byte content.
    @param test_csv_file A bytes-like object representing the content to be hashed.
    @dev This test creates an MD5 hash using both the generate_hash_file function and hashlib.md5 directly,
         and verifies that both hashes are identical.
    @return None
    """
    try:
        # Call generate_hash_file function
        hash = generate_hash_file(test_csv_file)

        # Compute MD5 hash using hashlib directly
        md5_hash = hashlib.md5()
        md5_hash.update(test_csv_file)

        # Assert that both hashes are identical
        assert hash == md5_hash.hexdigest(), "Hashes do not match"

    except Exception as e:
        raise RuntimeError(f"Error during test execution: {e}")
