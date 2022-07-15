from datetime import date, datetime, time
import time
from prettytable import PrettyTable
import os

## GLOBAL VARIABLES ##
TIME_FORMAT = "%H:%M"
todo_list = []
completed_list = []


## DISPLAY TODO LIST AS FORMATTED TABLE, SHOW USER OPTIONS ##
def todo_home():
    os.system('cls' if os.name == 'nt' else 'clear')
    sort_by_deadline()
    dt_now = datetime.now()
    day_name = dt_now.strftime("%A")
    date_today = date.today()
    time_now_str = datetime.now().strftime(TIME_FORMAT)

    todo_table = PrettyTable()
    todo_table.field_names = ["ID#", "Task", "Deadline", "Time remaining"]
    if len(todo_list) < 1:
        todo_table.add_row(["-", "No current tasks", "-", "-"])    
    else:
        for task in todo_list:
            index = task[0]
            name = task[1]
            deadline = task[2]
            rem_time = calculate_rem_time(deadline)
            if deadline == None:
                todo_table.add_row([index, name, "-", "-"])
            else:
                todo_table.add_row([index, name, deadline, rem_time])

    home_display = f"\n----TO-DO LIST APP----\nDate: {day_name}, {date_today}\nTime: {time_now_str}\n\n----CURRENT TASKS----\n{todo_table}\nOptions:\n[A] Add a task\n[M] Mark as done\n[D] Delete a task\n[C] View completed list\n[R] Refresh\n[X] Exit program"

    return home_display


## SORT TODO LIST BY DEADLINE ##
def sort_by_deadline():
    todo_list.sort(key=lambda x: (x[2] is None, x[2]))


## CALCULATE REMAINING TIMEDELTA FROM DEADLINE AND CURRENT TIME ##
def calculate_rem_time(deadline):
    if deadline:
        datetime_now = datetime.now()
        deadline_dt = datetime.combine(date.today(), deadline)
        if deadline_dt > datetime_now:
            delta = deadline_dt - datetime_now
            seconds = delta.seconds
            delta_dt = time.gmtime(seconds)
            rem_time = time.strftime(TIME_FORMAT, delta_dt)
        else:
            return "OVERDUE"
    else:
        rem_time = None
        
    return rem_time


## GETS USER INPUT USING A UNIQUE PROMPT WHEN CALLED ##
def get_input(prompt):
    user_input = input(prompt)
    return user_input


## GRACEFULLY EXIT PROGRAM WITH CONFIRMATION PROMPT AND FAREWELL MESSAGE ##
def exit_program():
    confirmation = get_input("Are you sure you want to quit? [y/n]:\n> ")
    if confirmation == "y":
        print("Have a great day!")
        quit()
    else:
        return


## REFRESH TODO HOME ##
def refresh():
    todo_home()


## USER CHOOSES OPTION FROM A DICTIONARY OF FUNCTION NAMES ##
def choose_option():
    options = {
        "A": add_task,
        "M": mark_as_done,
        "D": delete_task,
        "C": print_completed,
        "R": refresh,
        "X": exit_program
    }
    valid_option = False
    while not valid_option:
        option = get_input("> ")
        if option not in options:
            print("Invalid option")
        else:
            valid_option = True
            return options[option]


## ADD TASK TO TODO LIST WITH NAME AND DEADLINE VALUES ##
def add_task(index, name):
    deadline = False
    while deadline == False:
        option = get_input("Does the task have a deadline? [y/n]:\n> ")
        if option == "y":
            deadline = get_deadline()
        elif option == "n":
            deadline = None
        else:
            print("ERROR: Invalid input")

    task = [index, name, deadline]
    todo_list.append(task)


## GET DEADLINE TIME FROM USER INPUT ##
def get_deadline():
    valid_input = False
    while not valid_input:
        deadline_input = get_input("Enter deadline [HH:MM]:\n> ")
        try: 
            deadline = datetime.strptime(deadline_input, TIME_FORMAT).time()
            if deadline < datetime.now().time():
                print("ERROR: Time must be in the future")
            else:
                valid_input = True          
        except ValueError:
                print("ERROR: Invalid time format")

    return deadline


## MARK A TASK AS COMPLETE, ADD TO COMPLETED LIST AND REMOVE FROM TODO LIST ##
def mark_as_done():
    task_id = ""
    while task_id != "back":
        task_id = get_input("Enter ID# of completed task ([back] to cancel):\n> ")
        for i in todo_list:
            if task_id == str(i[0]):
                time_added_str = datetime.now().strftime(TIME_FORMAT)
                completed_task = (i[1], time_added_str)
                completed_list.append(completed_task)
                todo_list.remove(i)
                return completed_list
        else:
            print("ERROR: No existing task")  


## DELETE TASK FROM TODO LIST ##
def delete_task():
    task = get_input("Enter ID# of task to delete ([back] to cancel):\n> ")
    for i in todo_list:
        if task == str(i[0]):
            todo_list.remove(i)
            break
    else:
        print("ERROR: No existing task")
    

## DISPLAY COMPLETED TASKS IN A FORMATTED TABLE ##
def print_completed():
    os.system('cls' if os.name == 'nt' else 'clear')
    dt_now = datetime.now()
    day_name = dt_now.strftime("%A")
    date_today = date.today()
    time_now_str = datetime.now().strftime(TIME_FORMAT)
    completed_table = PrettyTable()
    completed_table.field_names = ["Task", "Time completed"]
    if len(completed_list) >= 1:
        for task in completed_list:       
            completed_table.add_row([task[0], task[1]])
    else:
        completed_table.add_row(["No completed tasks", "-"])         
    display = f"\n----TO-DO LIST APP----\nDate: {day_name}, {date_today}\nTime: {time_now_str}\n\n----COMPLETED TASKS----\n{completed_table}"
    print(display)
    option = get_input("Enter any key to continue:\n> ")

    if option:
        return


## MAIN PROGRAM LOOP ##
def main_loop():
    index = 0
    while True:
        print(todo_home())
        option = choose_option()
        if option == add_task:
            name = get_input("Enter task:\n> ")
            index += 1
            option(index, name)
        else:
            option()

main_loop()