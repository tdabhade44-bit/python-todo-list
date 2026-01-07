tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

def add_task():
    task_name = input("Enter task description: ")
    task = {
        "task": task_name,
        "done": False
    }
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks):
        status = "✔ Done" if task["done"] else "❌ Not Done"
        print(f"{index + 1}. {task['task']} - {status}")

def complete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark completed: "))
        tasks[task_no - 1]["done"] = True
        print("Task marked as completed!")
    except:
        print("Invalid input.")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
