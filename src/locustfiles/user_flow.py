from locust import HttpUser, SequentialTaskSet, task

from src.utils.data_generator import generate_user_dict
class UserFlow(SequentialTaskSet):
    @task
    def server_is_alive(self):
        self.client.get("/get")

    @task
    def post_user_dict(self):
        user_dict = generate_user_dict()
        self.client.post("/get", json=user_dict)

    @task
    def get_user_dict(self):
        self.client.get("/get")



class WebsiteUser(HttpUser):
    tasks = [UserFlow]
    wait_time = None