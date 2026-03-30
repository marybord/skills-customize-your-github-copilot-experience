from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

items = [
    {"id": 1, "name": "Notebook", "description": "A blank notebook", "price": 3.5, "in_stock": True},
    {"id": 2, "name": "Pen", "description": "Blue ink pen", "price": 1.2, "in_stock": True},
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}

@app.get("/items/")
def read_items(q: Optional[str] = None, limit: int = 10):
    results = items
    if q:
        results = [item for item in items if q.lower() in item["name"].lower()]
    return results[:limit]

@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/items/")
def create_item(item: Item):
    if item.price <= 0:
        return {"error": "Price must be greater than 0."}

    new_item = item.dict()
    new_item["id"] = len(items) + 1
    items.append(new_item)
    return new_item
