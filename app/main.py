#creating the array for temproray memory
todos =  []
#initalizing id to 0
id_counter = 1

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
    print("task succesfully added")
    return task
#view all tasks
def view_all_tasks():
    return todos

#view tasks by id
def completed_tasks(task_id: int):
    for task in todos:
        if task["id"] == task_id:
            task["completed"] = True
            return task
    return None

#delete task
def delete_task(task_id: int):
    for task in todos:
        if task["id"] == task_id:
            todos.remove(task)
            return todos
    return None 

while True:
    print("==========================")
    print("> Welcome, I am tort your to do list app\n")
    print("> This is the command center:\n")
    print("> Press [1] to create new task\n")
    print("> press [2] to view all tasks\n")
    print("> press [3] to delete task\n")
    print("> press[4] to exit\n")

    user_input = int(input(" > Your command : "))

    if user_input == 1:
        task = input("> input task : ")
        add_task(task)
    elif user_input == 2:
        tasks = view_all_tasks()
        print(tasks)
    elif user_input == 3:
        task_id = input("> delete task by id : ")
        delete_task(task_id)
    elif user_input == 4:
        print("app closed")
        break
    else:
        break
    