# FastAPI automated tests

from fastapi.testclient import TestClient

from main import app


def test_health_endpoint():
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200

def test_ready_endpoint():
    with TestClient(app) as client:
        response = client.get("/ready")
        assert response.status_code == 200    