from locust import HttpUser, task
from faker import Faker

fake = Faker()


class SimpleUser(HttpUser):
    @task(4)
    def get_request(self):
        self.client.get("/get")

    @task(1)
    def post_request(self):
        data = {
            "id": fake.random_int(1, 1000),
            "name": fake.name(),
            "email": fake.email()
        }
        self.client.post("/post", json=data)