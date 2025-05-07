from pydantic import BaseModel
from typing import Optional, List

class Address(BaseModel):
    street: str
    city: str
    postalCode: str

class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address # This is Nested Model Referencing

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None # This is Self Referencing

# This Phenomenon of Self and Nested Referencing is known as Forward Referencing

Comment.model_rebuild()

address = Address(
    street='Geeta Nagar',
    city='Solapur',
    postalCode='413006',
)

user = User(
    id=1,
    name='Paras Munoli',
    email='admin@gmail.com',
    address=address,
)

comment = Comment(
    id=1,
    content='Hello Welcome to My Github Repo',
    replies=[
        Comment(id=2,content='Hello Welcome to My Github Repo 2',)
    ],
)