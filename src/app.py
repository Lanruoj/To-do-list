from datetime import date, datetime, time, timedelta
from prettytable import PrettyTable

## GLOBAL VARIABLES ##
date_now = date.today()
time_now = datetime.now().strftime("%H:%M:%S")
todo_list = []

## HOME ##
def todo_home():
    # todo_table = PrettyTable()
    # todo_table.field_names = ["Task", "Deadline", "Time remaining"]
    print(todo_list)
    

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

## ADD TASK TO LIST ##
def add_task():
    time_format = "%H:%M"
    time_added = datetime.now().strftime(time_format)
    name = get_input("Enter task\n>")
    ### FIX
    deadline = "0"
    has_deadline = get_input("Does this task have a deadline? [y/n]\n>")
    deadline_input = ""
    if has_deadline=="y":
        while deadline < time_added: ### use a different condition!
            deadline_input = get_input("Enter deadline\n>")
            ## CHECK IF deadline_input MATCHES time_format ##
            try: 
                deadline_obj = datetime.strptime(deadline_input, time_format)
                deadline = datetime.strftime(deadline_obj, time_format)
                if deadline < time_added:
                    print("Time must be in the future")
                else:
                    break

            except ValueError:
                    print("Invalid time format")


    ## CREATE TASK OBJECT AS A TUPLE OF VALUES
    task = (name, time_added, deadline)
    ## ADD TASK TO GLOBAL LIST
    todo_list.append(task)


## EXTRACT deadline FROM task TUPLE ##
def extract_deadline(task):
    return task[2] 

## SORT LIST BY DEADLINE TIME ##
def sort_by_deadline():
    todo_list.sort(key=extract_deadline)



def mark_as_done():
    pass

def delete_task():
    pass

def print_completed():
    pass

def exit_program():
    pass


# MAIN PROGRAM LOOP
def main_loop():
    while True:
        todo_home()
        choose_option()

main_loop()