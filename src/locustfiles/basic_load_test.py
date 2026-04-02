from locust import HttpUser, task

from src.utils.data_generator import generate_user_dict


class WebsiteUser(HttpUser):
    @task(4)
    def get_root(self):
         self.client.get("/get")

    @task(1)
    def post_root(self):
        user = generate_user_dict()
        self.client.post("/post", json=user)
