from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": "sample"}


@app.post("/items")
def create_item(item: Item):
    return item


@app.get("/items")
def get_items():
    return [
        Item(name="Laptop", price=55000),
        Item(name="Mouse", price=800),
        Item(name="Keyboard", price=1500)
    ]