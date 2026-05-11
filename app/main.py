#creating the array for temproray memory
todos =  []
#initalizing id to 0
id_counter = 0

#create task
def add_task(title: str):
    global id_counter
    task =  {
        "id":id_counter,
        "title":title,
        "completed":False
    }
    todos.append(task)
    id_counter += 1
    return task
#view all tasks
def view_all_tasks():
    return todos

#view tasks by id
def completed_tasks(task_id: int):
    for task in todos:
        if task["id"] == task_id:
            task["completed"] == True
            return task

#update task

#delete task

#mark task as complete

#mark task as incomplete

#view all incomplete tasks

#view all complete task

while True:
    print("==========================")
    print("> Welcome, I am tort your to do list app\n")
    print("> This is the command center:\n")
    print("> Press [1] to create new task\n")
    print("> press [2] to view all tasks\n")
    print("> press [3] to exit")

    user_input = input(" > Your command : ")