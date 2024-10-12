from fastapi import Depends, FastAPI, HTTPException, status
from .db import engine, SQLModel


from app.routers import users


app = FastAPI()

app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

SQLModel.metadata.create_all(engine)