import pytest
from app import create_app  # Adjust the import based on your app structure

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test that the home page loads and contains expected elements."""
    response = client.get('/')
    assert response.status_code == 200

    html = response.get_data(as_text=True)
    assert "Simple Weather App" in html
    assert "Check Weather" in html

