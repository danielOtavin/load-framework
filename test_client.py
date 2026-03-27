from src.clients.http_client import HttpClient

with HttpClient("http://localhost:8000") as client:
    resp = client.get("/get")
    print(f"Status: {resp.status_code}")
    print(f"Response: {resp.json()}")
