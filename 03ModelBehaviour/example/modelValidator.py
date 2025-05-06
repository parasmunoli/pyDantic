from pydantic import BaseModel, field_validator, model_validator, computed_field

class User(BaseModel):
    id: int
    username: str

    @field_validator('username')
    def validate_username(self, value):
        if len(value) < 3:
            raise ValueError('Username must be at least 3 characters long')
        return value

class SignupData(BaseModel):
    email: str
    password: str
    confirmPassword: str

    @model_validator(mode='after')
    def validate_password(self, values):
        if len(values.password) < 8:
            raise ValueError('Password must be at least 3 characters long')

        if values.password != values.confirmPassword:
            raise ValueError('Passwords do not match')

        return values

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity