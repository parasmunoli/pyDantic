from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()

class User(BaseModel):
    id: int
    userName: str
    email: EmailStr
    password: str
class Settings(BaseModel):
    app_name: str = "Awesome API"
    admin_email: EmailStr = "admin@gmail.com"

def get_settings():
    return Settings()

@app.post("/signup")
def signup(user: User):
    return {"message": f"User with {user.userName} signed up successfully!"}

@app.get("/settings")
def settings_endpoint(settings: Settings = Depends(get_settings)):
    return settings
