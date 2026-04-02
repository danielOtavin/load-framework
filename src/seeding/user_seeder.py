from src.utils.data_generator import generate_user_dict
from src.clients.http_client import HttpClient


def user_seeding(count: int = 50) -> list:
    client = HttpClient(base_url="http://localhost:8000", log=False)
    users = []

    for i in range(count):
        user_dict = generate_user_dict()
        response = client.post("/post", json=user_dict)
        if response.status_code == 200:
            users.append(user_dict)

        if i % 10 == 0:
            print(f'Создано {i} пользователей')

    client.close()
    print(f'Создано {len(users)} из {count} пользователей')
    return users
