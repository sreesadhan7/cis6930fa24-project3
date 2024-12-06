import os
import sys
import tempfile
import pytest

# Add the absolute path to the project root directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../project3')))
from app import app, fetch_incidents, extract_incidents, cluster_and_visualize

@pytest.fixture
def test_client():
    """
    Set up a test client for the Flask app and a temporary upload folder.
    """
    app.config['TESTING'] = True
    app.config['UPLOAD_FOLDER'] = tempfile.mkdtemp()
    client = app.test_client()
    yield client

    # Clean up the temporary folder
    for file in os.listdir(app.config['UPLOAD_FOLDER']):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file))
    os.rmdir(app.config['UPLOAD_FOLDER'])


def test_error_handling(test_client):
    """
    Test error handling for invalid URLs and non-PDF files.
    """
    invalid_urls = [
        "https://example.com/not_a_pdf",
        "https://nonexistent.url.com/incident.pdf"
    ]
    invalid_files = ["not_a_pdf.txt"]

    # Test invalid URLs
    for url in invalid_urls:
        with pytest.raises(Exception):
            fetch_incidents(url)

    # Test invalid file uploads
    for invalid_file in invalid_files:
        with open(os.path.join(app.config['UPLOAD_FOLDER'], invalid_file), 'w') as f:
            f.write("This is not a valid PDF content")
        with pytest.raises(Exception):
            extract_incidents(os.path.join(app.config['UPLOAD_FOLDER'], invalid_file))  