import pytest
from src.main import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_tasks(client):
    """Verifies baseline fetch behavior."""
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.get_json()) >= 2

# TODO: Add edge-case assertion ensuring bad JSON payloads trigger explicit 400 structures.
