# Third Party
from fastapi.testclient import TestClient
import pytest

# First Party
from app.main import app

client = TestClient(app)


@pytest.fixture
def test_client() -> TestClient:
    """Fixture for creating a test client."""
    return TestClient(app)


def test_health_check(test_client: TestClient):
    """Test the health check endpoint."""
    response = test_client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}
