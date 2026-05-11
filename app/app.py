from fastapi import FastAPI
from pydantic import BaseModel
import main

app = FastAPI()

#declaring input input schema

class TaskInput(BaseModel):
    title: str

#creating path operations for all commands

@app.post("/task/create")
def create_task():
    """creating new task"""
    return main.add_task()

