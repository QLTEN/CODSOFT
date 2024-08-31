# To-Do List Application in Python (Command-Line Version)

todo_list = []

def add_task(task):
    todo_list.append({"task": task, "completed": False})
    print(f'Task "{task}" added successfully!')

def view_tasks():
    if not todo_list:
        print("No tasks in the list!")
    else:
        for idx, task in enumerate(todo_list, start=1):
            status = "Done" if task["completed"] else "Pending"
            print(f'{idx}. {task["task"]} - {status}')

def update_task(task_number, updated_task):
    if 0 < task_number <= len(todo_list):
        todo_list[task_number - 1]["task"] = updated_task
        print(f'Task {task_number} updated to "{updated_task}"!')
    else:
        print("Invalid task number!")

def delete_task(task_number):
    if 0 < task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f'Task "{removed_task["task"]}" deleted!')
    else:
        print("Invalid task number!")

def mark_as_completed(task_number):
    if 0 < task_number <= len(todo_list):
        todo_list[task_number - 1]["completed"] = True
        print(f'Task {task_number} marked as completed!')
    else:
        print("Invalid task number!")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark as Completed")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to update: "))
            updated_task = input("Enter the updated task: ")
            update_task(task_number, updated_task)
        elif choice == "4":
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == "5":
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_as_completed(task_number)
        elif choice == "6":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
