from datetime import date, datetime, time, timedelta
import re

## GLOBAL VARIABLES
date_now = date.today()
time_now = datetime.now().strftime("%H:%M:%S")

##

# Gets user input, using different prompt messages
def get_input(prompt):
    user_input = input(prompt)
    return user_input

# User chooses what they'd like the program to do via user input
def choose_option():
    options = {
        "A": add_task,
        "M": mark_as_done,
        "D": delete_task,
        "C": print_completed,
        "X": exit_program
    }
    while True:
        option = get_input(">")
        if option not in options:
            print("Invalid option")
        else:
            return options[option]()

######

def add_task():
    time_added = datetime.now().strftime("%H:%M:%S")
    name = get_input("Enter task\n>")
    has_deadline = get_input("Does this task have a deadline? [y/n]\n>")
    deadline_input = get_input("Enter deadline\n>")
    deadline_obj = datetime.strptime(deadline_input, "%H:%M")
    deadline = datetime.strftime(deadline_obj, "%H:%M")
    print(deadline)

    task = (name, time_added, deadline)
    print(task)


add_task()





def mark_as_done():
    pass

def delete_task():
    pass

def print_completed():
    pass

def exit_program():
    pass

def sort_list():
    pass

def todo_home():
    pass


# MAIN PROGRAM LOOP
def main_loop():
    pass