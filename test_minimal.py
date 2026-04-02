from locust import HttpUser, task

class MinimalUser(HttpUser):
    @task(10)
    def get_root(self):
        self.client.get("/get")

    @task(1)
    def post_root(self):
        self.client.post("/post")