from fastapi import FastAPI
from src.utils.db import Base, engine
from src.user.router import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

app.include_router(user_router)
