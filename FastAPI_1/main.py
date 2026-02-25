from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str
    origin: str

teas: List[Tea] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tea API!"}

@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def create_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{id}")
def update_tea(id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == id:
            teas[index] = updated_tea
            return tea
    return {"message": "Tea not found"}

@app.delete("/teas/{id}")
def delete_tea(id: int):
    for index, tea in enumerate(teas):
        if tea.id == id:
            delete = teas.pop(index)
            return {"message": "Tea deleted successfully {delete}"}
    return {"message": "Tea not found"}
