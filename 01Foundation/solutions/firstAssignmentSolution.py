from pydantic import BaseModel

# TODO: Create Product model with id, name, price, in_stock

class Product(BaseModel):
    id: int
    name: str
    price: float
    inStock: bool

Data = {
    'id': 102,
    'name': 'Keyboard',
    'price': 3750,
    'inStock': False
}

validateData = Product(**Data)
print(validateData)