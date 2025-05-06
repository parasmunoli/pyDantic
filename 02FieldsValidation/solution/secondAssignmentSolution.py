from pydantic import BaseModel, Field
from typing import Optional

# TODO: Create Employee model
# Fields:
# - id: int
# - name: str (min 3 chars)
# - department: optional str (default 'General')
# - salary: float (must be >= 10000)

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        title='Employee ID',
        description='Employee ID',
        min_length=3,
        max_length=50,
    )
    department: Optional[str] = 'General'
    salary: float = Field(..., gt=10000)

data = {
    'id': 2,
    'name': 'Paras Munoli',
    'salary': 20000
}

employee = Employee(**data)
print(employee)