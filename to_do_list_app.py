def add_task():
    print()
    try:
        amount_tasks = int(input("How many tasks would you like to add?"))
        try:
            for i in range(amount_tasks):
                task = input("Enter the task you would like to add to the list:\n")
                if task not in to_do_list:
                    to_do_list.append({"Task": task, "Complete": False})
                    print(f"{task} added to To-Do list.")
            else:
                print("This task is already on your To-Do list.")
        except ValueError:
            ("Invalid data type. Please enter a number.")

    except ValueError:
        pass


def view_tasks():
    for item in to_do_list:
        print(item)


def complete_task():
    pass


def delete_task():
    task = user_delete
    if task in to_do_list:
        to_do_list.remove(task)
        print(f"'{task}' has been removed from the list.")
    else:
        print(f"Sorry, '{task}' was not found in the list...")


to_do_list = []
print("-----Welcome to the To-Do List App!-----")
while True:
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")
    user_choice = int(input("Enter choice:\n"))

    if user_choice == 1:
        add_task()
    elif user_choice == 2:
        view_tasks()
    elif user_choice == 3:
        user_complete = input("Which task would you like to mark as complete?\n")
        complete_task()
    elif user_choice == 4:
        user_delete = input("Enter the task you would like to delete from the list:\n")
        delete_task()
    elif user_choice == 5:
        print("Have a nice day!")
        break
    else:
        print("Please enter a valid choice from the list [1-5]")
