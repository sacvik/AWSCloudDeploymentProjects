from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict():
    response = client.post(
        "/predict", json={"text": "This is a sample news article"}
    )
    assert response.status_code == 200
    assert "prediction" in response.json()
