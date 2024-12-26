from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# use this model for validatation or structure the data
class Item(BaseModel):
   text: str = None
   is_done: bool = False

app = FastAPI()

# add todo list items array
items=[]

# it is use for get the directory of https and its i root direc
@app.get("/")
def root():
    return{"hello": "developer"}

# create a list of items 
@app.post("/items")

def create_item(item :Item):
    items.append(item)
    return items

# limits of items 
# use response model to interact from frontend client with fast api

@app.get("/items",response_model=list[Item])
def list_item(limit: int =10):
    return items[0:limit]

# get a list of items by id 
# use response model to interact from frontend client with fast api
@app.get("/items/{item_id}",response_model=Item)
def get_item(item_id :int) -> Item:
  if item_id< len(items):
     return items[item_id]
  else:
     raise HTTPException(status_code=404,detail=f"Item {item_id} NOt found")

