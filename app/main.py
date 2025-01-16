from fastapi import FastAPI
from fastapi import APIRouter
from app.routers import user, task

app = FastAPI()

#python3 -m uvicorn main:app
#uvicorn main:app --reload
#python -m uvicorn main:app

@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)