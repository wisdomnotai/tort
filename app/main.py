# =========================
# TORT APP
# =========================

todos = []
id_counter = 1


# =========================
# TASK FUNCTIONS
# =========================

def add_task(title: str):
    """
    Create a new task and store it in memory.
    """
    global id_counter

    task = {
        "id": id_counter,
        "title": title.strip(),
        "completed": False
    }

    todos.append(task)
    id_counter += 1

    print("\n[✓] Task added successfully.\n")


def view_all_tasks():
    """
    Display all tasks.
    """
    if not todos:
        print("\n[!] No tasks available.\n")
        return

    print("\n========== YOUR TASKS ==========\n")

    for task in todos:
        status = "✓ Completed" if task["completed"] else "• Pending"

        print(f"""
ID        : {task['id']}
Title     : {task['title']}
Status    : {status}
--------------------------------
""")


def get_task_by_id(task_id: int):
    """
    Find a task using its ID.
    """
    for task in todos:
        if task["id"] == task_id:
            return task

    return None


def complete_task(task_id: int):
    """
    Mark a task as completed.
    """
    task = get_task_by_id(task_id)

    if task:
        task["completed"] = True
        print("\n[✓] Task marked as completed.\n")
    else:
        print("\n[!] Task not found.\n")


def delete_task(task_id: int):
    """
    Delete a task by ID.
    """
    task = get_task_by_id(task_id)

    if task:
        todos.remove(task)
        print("\n[✓] Task deleted successfully.\n")
    else:
        print("\n[!] Task not found.\n")


# =========================
# MAIN APP LOOP
# =========================

while True:

    print("""
==============================
        TORT TODO APP
==============================

[1] Create New Task
[2] View All Tasks
[3] Complete Task
[4] Delete Task
[5] Exit
""")

    try:
        user_input = int(input("> Enter command: "))

        # CREATE TASK
        if user_input == 1:
            title = input("\n> Enter task title: ")

            if not title.strip():
                print("\n[!] Task title cannot be empty.\n")
                continue

            add_task(title)

        # VIEW TASKS
        elif user_input == 2:
            view_all_tasks()

        # COMPLETE TASK
        elif user_input == 3:
            task_id = int(input("\n> Enter task ID to complete: "))
            complete_task(task_id)

        # DELETE TASK
        elif user_input == 4:
            task_id = int(input("\n> Enter task ID to delete: "))
            delete_task(task_id)

        # EXIT
        elif user_input == 5:
            print("\nGoodbye.\n")
            break

        else:
            print("\n[!] Invalid command.\n")

    except ValueError:
        print("\n[!] Please enter a valid number.\n")