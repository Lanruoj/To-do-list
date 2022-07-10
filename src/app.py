from datetime import date, datetime, time, timedelta
import re

## GLOBAL VARIABLES
date_now = date.today()
time_now = datetime.now().strftime("%H:%M:%S")
todo_list = []

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
    time_format = "%H:%M"
    time_added = datetime.now().strftime(time_format)
    name = get_input("Enter task\n>")
    deadline = "00:00"
    has_deadline = get_input("Does this task have a deadline? [y/n]\n>")
    deadline_input = ""
    if has_deadline=="y":
        while deadline < time_added: ### use a different condition!
            # while True:
            deadline_input = get_input("Enter deadline\n>")
            # CHECK IF deadline_input MATCHES time_format
            try: 
                deadline_obj = datetime.strptime(deadline_input, time_format)
                deadline = datetime.strftime(deadline_obj, time_format)

            except ValueError:
                print("Invalid time format")
                
            if deadline < time_added:
                print("Time must be in the future")

    # print("out of loop")
    task = (name, time_added, deadline)
    todo_list.append(task)
    # print(task)


add_task()
print(todo_list)
# PRINT THE 2ND INDEX OF task IN todo_list
print([task[2] for task in todo_list])

add_task()
print(todo_list)
# PRINT THE 2ND INDEX OF task IN todo_list
print([task[2] for task in todo_list])





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