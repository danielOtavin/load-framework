from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    http_base_url: str = "http://localhost:8000"
    grpc_host: str = "localhost"
    grpc_port: int = 50051
    log_enabled: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()