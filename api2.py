from typing import Union 

from fastapi import FastAPI

app = FastAPI()

fake_customers_db = [{'item_name': 'Maria'},{'item_name': 'Nascimento'},{'item_name': 'Raimundo' }, {'item_name': 'Assis'}, {'item_name': 'Gerlane'}]

@app.get("/cusomers/")
def read_item(skip : int = 0, limit : int = 10):
      return fake_customers_db[skip:skip + limit]