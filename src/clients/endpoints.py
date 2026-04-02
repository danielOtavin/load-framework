from enum import Enum

class ApiEndpoint(str, Enum):
    GET_USER = "/users/{user_id}"
    CREATE_USER = "/users"
    HEALTH = "/health"