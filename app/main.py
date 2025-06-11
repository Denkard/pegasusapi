# Modules Mapping
import sys
sys.path.insert(0, '/workspace/project/pegasusapi/pegasusapi-1/mongodb')

# Others
from mongo_connect import connect_mongodb
from bson import ObjectId
from typing import Union
from fastapi import FastAPI

mongo = connect_mongodb()
app = FastAPI()


@app.get("/")
def read_root():
    return mongo.whitebook.pages.find_one({})
    #return {"Hello": "Teste"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}