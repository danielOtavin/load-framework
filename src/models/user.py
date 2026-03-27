from pydantic import BaseModel, Field, ValidationError

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    email: str
    is_active: bool = True

def validate_user(data: dict):
    try:
        return User(**data)
    except ValidationError as e:
        print(f"Validation error: {e}")
        return None

bad_data = {"id": "not_int", "name": "J", "email": "not_email"}
print(validate_user(bad_data))