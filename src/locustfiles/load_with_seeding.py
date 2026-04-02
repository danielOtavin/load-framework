from locust import HttpUser, task
from src.seeding.user_seeder import user_seeding

USERS = user_seeding(count=50)


class User(HttpUser):
    @task
    def get_request(self):
        self.client.get("/get")

    @task
    def post_request(self):
        # Используем случайного пользователя из сидинга
        import random
        user = random.choice(USERS)
        self.client.post("/post", json=user)