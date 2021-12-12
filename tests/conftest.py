from main import app
from fastapi.testclient import TestClient

def test_app():
    
    client = TestClient(app)
    return client

test_app = test_app()