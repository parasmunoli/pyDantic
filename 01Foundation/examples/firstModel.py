from pydantic import BaseModel, Field

class User(BaseModel):
    fName: str
    lName: str
    age: int
    email: str = Field(..., alias='email', pattern=r'.*@gmail\.com')

Data = {
    'fName': 'Paras',
    'lName': 'Munoli',
    'age': 22,
    'email': 'parasmunoli@gmail.com'
}

# ** is expansion Operator
user = User(**Data)
print(user)
