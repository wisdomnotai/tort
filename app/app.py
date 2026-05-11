from fastapi import FastAPI, status, HTTPException
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

@app.get("/tasks/retrieve")
def get_task():
    """viewing all tasks"""
    return main.view_all_tasks

@app.patch("/task/{task_id}/complete")
def update_task(task_id: int):
    """marking task complete by id"""
    task = main.complete_task(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{task_id} not found")
    return task

