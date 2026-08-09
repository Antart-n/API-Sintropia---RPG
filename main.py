from fastapi import FastAPI
from pydantic import BaseModel
import loadjson

app = FastAPI()

data = loadjson.load()

class upd(BaseModel):
    item: str | int | float | list

@app.get("/characters")
def characters():
    return data

@app.get("/characters/{name}")
def character(name: str):
    return data[name]

@app.get("/characters/{name}/{statistic}")
def statistic(name: str, statistic: str):
    return data[name][statistic]

@app.put("/characters/{name}/{statistic}/{item}")
def update_item(dados: upd, name: str, statistic: str, item: str):
    if name in data and statistic in data[name] and item in data [name][statistic]:
        data[name][statistic][item] = dados.item
        loadjson.save(data)
    return loadjson.load()

@app.put("/characters/{name}/{statistic}")
def update_item(dados: upd, name: str, statistic: str):
    if name in data and statistic in data[name]:
        data[name][statistic] = dados.item
        loadjson.save(data)
    return loadjson.load()
