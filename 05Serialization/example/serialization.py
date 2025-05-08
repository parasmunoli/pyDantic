from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    state: str
    pincode: str
    country: str

class User(BaseModel):
    id: int
    name: str
    email: str
    isActive: bool = True
    createdAt: datetime
    address: Address
    skills: List[str] = []
    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")
        }
    )

# Creating a user Instance

address= Address(
    street='35/9 west side',
    city='Solapur',
    state='Maharashtra',
    pincode='123456',
    country='India'
)

user1 = User(
    id=1,
    name='Paras Munoli',
    email='admin@gmail.com',
    createdAt=datetime.now(),
    address=address,
    skills=["Python", "JavaScript", "Java", "NodeJSS"],
)

# Using model_dump() expected O/P Dict

pythonDict = user1.model_dump()
print(pythonDict)

# Using model_dump_json() expected O/P JSON
jsonDict = user1.model_dump_json()
print(jsonDict)