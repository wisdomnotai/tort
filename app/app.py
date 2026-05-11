from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

import main


# =========================
# FASTAPI INSTANCE
# =========================

app = FastAPI(
    title="Todo API",
    description="A simple Todo API built with FastAPI",
    version="1.0.0"
)


# =========================
# REQUEST SCHEMA
# =========================

class TaskInput(BaseModel):
    title: str


# =========================
# HOME ROUTE
# =========================

@app.get("/")
def home():

    return {
        "message": "Welcome to the Todo API"
    }


# =========================
# CREATE TASK
# =========================

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskInput):

    new_task = main.add_task(task.title)

    return {
        "message": "Task created successfully",
        "task": new_task
    }


# =========================
# GET ALL TASKS
# =========================

@app.get("/tasks")
def get_tasks():

    return {
        "tasks": main.view_all_tasks()
    }


# =========================
# GET TASK BY ID
# =========================

@app.get("/tasks/{task_id}")
def get_single_task(task_id: int):

    task = main.get_task_by_id(task_id)

    if not task:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    return {
        "task": task
    }


# =========================
# COMPLETE TASK
# =========================

@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int):

    task = main.complete_task(task_id)

    if not task:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    return {
        "message": "Task marked as completed",
        "task": task
    }


# =========================
# DELETE TASK
# =========================

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    task = main.delete_task(task_id)

    if not task:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    return {
        "message": "Task deleted successfully"
    }