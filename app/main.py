from typing import Union

from fastapi import FastAPI

print("TESTE EXECUTANDO")
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Teste"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}