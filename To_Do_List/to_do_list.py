from os import name, system
from time import sleep

def c_t(): # A function that clears the user's terminal
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

tasks = []
menu = ["--- To-Do List Manager ---", "1. Add a new task", "2. Add an urgent task (placed at the beginning)",
         "3. See all the active tasks", "4. Task Completion (removes the task you will provide)", "5. Clear all tasks", "6. Save my tasks (as a tasks.txt file)", "7. Quit"]

while True:
    c_t()
    for i in menu:
        print(i, end = "\n")
    uc = int(input("Enter your choice (only a number): ")) # Reads the user's choice
    if uc == 1:
        new_task = input("Enter the name of the new task you want to create: ")
        new_task = new_task.strip().lower()
        tasks.append(new_task)
        print(f"{new_task} inserted")
        sleep(1) # Waits for 1 second before clearing the terminal

    elif uc == 2:
        urgent_task = input("Enter the name of the urgent task you want to create: ")
        urgent_task = urgent_task.strip().lower()
        tasks.insert(0, urgent_task)
        print(f"{urgent_task} inserted")
        sleep(1) # Waits for 1 second before clearing the terminal

    elif uc == 3:
        if len(tasks) == 0:
            print("You have no active tasks.")
            sleep(1) # Waits for 1 second before clearing the terminal
        else:
            ctasks = tasks.copy()
            ctasks.sort() # Sorts the new list alphabetically
            print("The active tasks (sorted alphabetically) are: ")
            for i in range(len(ctasks)):
                print(f"{i+1}. {ctasks[i].capitalize()}")
            print()
            print("The active tasks (not sorted) are: ")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i].capitalize()}")
            sleep(5) # Waits for 5 seconds before clearing the terminal

    elif uc == 4:
        del_task = input("Enter the name of the task you want to remove (case - insensitive): ")
        del_task = del_task.lower().strip()
        if del_task in tasks:
            tasks.remove(del_task)
            print(f"{del_task.capitalize()} was successfully removed from the task list.")
        else:
            print(f"There is no such task")
        sleep(1) # Waits for 1 second before clearing the terminal

    elif uc == 5:
        while True:
            sure = input("This action will clear your task list! Are you sure(YES/NO)? ")
            sure = sure.upper().strip()
            if sure == "YES" or sure == "NO":
                break
            else:
                print("Please enter a valid input!")
        if sure == "YES":
            tasks.clear()
            print("Tasks were successfully cleared.")
        else:
            print("Process successfully aborted")
        sleep(2) # Waits for 2 seconds before clearing the terminal

    elif uc == 6:
        print("Your tasks were saved in a tasks.txt file.")
        with open("tasks.txt", "w") as f: # File creation
            ctasks = tasks.copy()
            ctasks.sort() # Sorts the new list alphabetically
            f.write("The active tasks (sorted alphabetically) are: ")
            f.write("\n")
            for i in range(len(ctasks)):
                f.write(f"{i+1}. {ctasks[i].capitalize()}")
                f.write("\n")
            f.write("\n")
            f.write("The active tasks (not sorted) are: ")
            f.write("\n")
            for i in range(len(tasks)):
                f.write(f"{i+1}. {tasks[i].capitalize()}")
                f.write("\n")
        sleep(1) # Waits for 1 second before clearing the terminal
    elif uc == 7:
        print("Going to quit in:")
        for i in range(1,4):
            print(i)
            sleep(1) # Waits for 1 second before clearing the terminal
        break