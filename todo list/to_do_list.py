# To-Do List Application: Create a simple to-do list application that allows users to add, remove, and view tasks. You can store tasks in a list or a text file.
# notes for additional features: compile the tasks or notes by date, can include also the day

import datetime
import sys
sys.stdout.reconfigure(encoding='utf-8')


def create_header(text):
    text_length = len(text)
    box_width = text_length + 4  # Add extra space for padding

    # Create the top border of the box
    top_border = "+" + "-" * box_width + "+"

    # Create the middle content of the box with text
    middle_content = f"| {text} |"

    # Create the bottom border of the box
    bottom_border = "+" + "-" * box_width + "+"

    # Print the header
    print(top_border)
    print(middle_content)
    print(bottom_border)


header_text = "TO DO LIST!"
create_header(header_text)


def add(task):
    timestamp = datetime.datetime.now().strftime("%A")
    with open("todo-list.txt", "a") as f:
        f.write(f" {timestamp} - {task}\n")


def mark_task_done(task_index):
    with open("todo-list.txt", "r+") as f:
        notes = f.readlines()
        if 0 < task_index <= len(notes):
            task = notes[task_index - 1].strip()
            # Check if the task is already marked as done
            if not task.startswith("DONE - "):
                # Mark the task as done by adding "DONE - " prefix
                notes[task_index - 1] = "DONE = " + task + "\n"
                f.seek(0)
                f.writelines(notes)
                f.truncate()


def view():
    with open("todo-list.txt", "r") as f:
        notes = f.readlines()
        if len(notes) == 0:
            print("No tasks in the to-do list.")
        else:
            print("Tasks:")
            for x, task in enumerate(notes, start=1):
                print(f"{x}.{task.strip()}")


while True:
    user = input("Do you want to add, remove or view task? ('q' to quit)? ")
    if user == "add":
        task = input("Add task: ")
        add(task)
    elif user == "remove":
        task_index = int(input("Enter the task number to mark as done: "))
        mark_task_done(task_index)
    elif user == "view":
        view()
    elif user == "q":
        break
    else:
        print("Invalid input. Please enter 'add', 'remove', 'view', or 'q' to quit.")
