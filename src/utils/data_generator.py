from faker import Faker
from src.models.user import User
from typing import Dict

fake = Faker()

def generate_user_dict() -> Dict:
    """Генерирует словарь с данными пользователя для POST-запросов"""
    return {
        "id": fake.random_int(min=1, max=10000),
        "name": fake.name(),
        "email": fake.email(),
        "is_active": fake.boolean()
    }

from src.utils.data_generator import generate_user_dict

user_data = generate_user_dict()
print(user_data)