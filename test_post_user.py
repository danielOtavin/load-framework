from src.clients.http_client import HttpClient
from src.utils.data_generator import generate_user_dict

with HttpClient("http://localhost:8000", log=True) as client:
    user = generate_user_dict()
    print(f"Sending: {user}")

    # httpbin /post эхо-возвращает отправленные данные
    response = client.post("/post", json=user)
    print(f"Response: {response.json()}")