import json   # Used for saving/loading tasks from file

todo_list = []   # This list will store all tasks


# function for LOAD TASKS
def load_tasks():
    global todo_list   # Allows us to modify global list
    try:
        # Try to open and read tasks from file
        with open("tasks.json", "r") as file:
            todo_list = json.load(file)
    except:
        # If file doesn't exist, start with empty list
        todo_list = []


# function for  SAVE TASKS
def save_tasks():
    # Save current tasks list into file
    with open("tasks.json", "w") as file:
        json.dump(todo_list, file)


# function for  ADD TASK
def add_task():
    # Take task name from user
    task = input("Enter the Task you want to add:\n")

    # Take category (Work/Personal)
    category = input("Enter category (Work/Personal):\n")

    # Add task as dictionary inside list
    todo_list.append({
        "task": task,
        "category": category,
        "Status": "Pending"   # Default status
    })

    save_tasks()   # Save after adding
    print(f"The task '{task}' has been added successfully!")


# function for  VIEW TASK
def view_task():
    # Check if list is empty
    if len(todo_list) == 0:
        print("No tasks in the list!")
    else:
        # Loop through all tasks and display them
        for index, task in enumerate(todo_list, 1):
            print(
                f"{index}: {task['task']} [{task['category']}] - {task['Status']}")


# function for  REMOVE TASK
def remove_task():
    if len(todo_list) == 0:
        print("\nList is empty! No task to remove!")
    else:
        try:
            # Ask user for task number
            search_index = int(input("Enter index to remove:\n")) - 1

            # Check if index is valid
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)   # Remove task
                save_tasks()   # Save changes
                print(f"Task '{removed_task['task']}' removed successfully!")
            else:
                print("Invalid index!")

        except ValueError:
            print("Invalid input!")


# function for task MARK DONE
def mark_done():
    if len(todo_list) == 0:
        print("\nList is empty! No task to mark!")
    else:
        try:
            # Ask user which task to mark completed
            search_index = int(input("Enter index to mark complete:\n")) - 1

            # Validate index
            if 0 <= search_index < len(todo_list):
                # Update status
                todo_list[search_index]["Status"] = "Completed"
                save_tasks()   # Save changes
                print(
                    f"Task '{todo_list[search_index]['task']}' marked completed!")
            else:
                print("Invalid index!")

        except ValueError:
            print("Invalid input!")


# function for task VIEW COMPLETED
def view_completed():
    found = False   # To check if any completed task exists
    print("\nCompleted Tasks:")

    # Loop through tasks
    for task in todo_list:
        if task["Status"] == "Completed":
            print(f"{task['task']} [{task['category']}]")
            found = True

    if not found:
        print("No completed tasks.")


# function for Filter Tasks
def filter_tasks():
    # Ask user for category
    cat = input("Enter category to filter:\n")

    found = False
    print("\nFiltered Tasks:")

    # Show only tasks matching category
    for task in todo_list:
        if task["category"].lower() == cat.lower():
            print(f"{task['task']} - {task['Status']}")
            found = True

    if not found:
        print("No tasks found in this category.")


# main function
def main():
    load_tasks()   # Load tasks when program starts

    print("Welcome to the To-Do List App!\n")

    while True:
        # Display menu
        print("\nMenu:")
        print("1. Add a New Task")
        print("2. View all tasks")
        print("3. Remove a Task")
        print("4. Mark Task as Completed")
        print("5. View Completed Tasks")
        print("6. Filter by Category")
        print("7. Exit")

        choice = input("Enter your choice (1-7):\n")

        # Call functions based on user choice
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            view_completed()
        elif choice == "6":
            filter_tasks()
        elif choice == "7":
            save_tasks()   # Save before exiting
            print("Exiting the To-Do List App!")
            break
        else:
            print("Invalid choice! Please enter 1-7.")


# Run the program
main()
