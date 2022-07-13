from datetime import date, datetime, time, timedelta
from prettytable import PrettyTable

## GLOBAL VARIABLES ##
time_format = "%H:%M"
todo_list = []
completed_list = []

# Gets user input, using different prompt messages
def get_input(prompt):
    user_input = input(prompt)
    if user_input == "X":
        quit()
    else:
        return user_input


# User chooses what they'd like the program to do via user input
def choose_option():
    options = {
        "A": add_task,
        "M": mark_as_done,
        "D": delete_task,
        "C": print_completed,
        # "X": exit_program
    }
    while True:
        option = get_input("> ")
        if option not in options:
            print("Invalid option")
        else:
            return options[option]


def mark_as_done():
    while True:
        task = get_input("Enter completed task ([back] to cancel)\n> ")
        for i in todo_list:
            if task == i[0]:
                time_added_str = datetime.now().strftime(time_format)
                completed_task = (i[0], time_added_str)
                completed_list.append(completed_task)
                todo_list.remove(i)
                return completed_list
        else:
            if task == "back":
                return 
            else:
                print("ERROR: No existing task")
                
    


def delete_task():
    task = get_input("Enter task to delete ([back] to cancel)\n> ")
    for i in todo_list:
        if task == i[0]:
            todo_list.remove(i)
            break
    else:
        print("ERROR: No existing task")
    


def print_completed():
    completed_table = PrettyTable()
    completed_table.field_names = ["Task", "Time completed"]

    for task in completed_list:       
        completed_table.add_row([task[0], task[1]])
    
    print(completed_table)
    option = get_input("Enter [y] to continue\n> ")
    if option == "y":
        todo_home()


## HOME ##
def todo_home():
    dt_now = datetime.now()
    day_name = dt_now.strftime("%A")
    sort_by_rem_time()
    date_today = date.today()
    time_now_str = datetime.now().strftime(time_format)
    todo_table = PrettyTable()
    todo_table.field_names = ["Task", "Deadline", "Time remaining"]

    if len(todo_list) < 1:
        todo_table.add_row(["No current tasks", "-", "-"])    
    else:
        for task in todo_list:
            name = task[0]
            deadline = task[1]
            rem_time = calculate_rem_time(deadline)
            if deadline == None:         
                todo_table.add_row([name, "-", "-"])
            else:
                todo_table.add_row([name, deadline, rem_time])

    home_display = f"\n----TO-DO LIST APP----\nDate: {day_name}, {date_today}\nTime: {time_now_str}\n{todo_table}\nOptions:\n[A] Add a task\n[M] Mark as done\n[D] Delete a task\n[C] View completed list\n[X] Exit program"
    return home_display
    

def get_deadline():
    while True:
        deadline_input = get_input("Enter deadline\n> ")
        ## CHECK IF deadline_input MATCHES time_format ##
        try: 
            deadline_obj = datetime.strptime(deadline_input, time_format).time()
            # deadline_str = datetime.strftime(deadline_input, time_format)
            if deadline_obj < datetime.now().time():
                print("ERROR: Time must be in the future")
            else:
                break           
        except ValueError:
                print("ERROR: Invalid time format")

    return deadline_obj


def add_task(name):
    deadline = False
    while deadline == False:
        option = get_input("Does the task have a deadline? [y/n]\n> ")
        if option == "y":
            deadline = get_deadline()
        elif option == "n":
            deadline = None
        else:
            print("ERROR: Invalid input")

    task = (name, deadline)
    todo_list.append(task)

def calculate_rem_time(deadline):
    if deadline != None:
        datetime_now = datetime.now()
        time_now_obj = datetime.now().time()
        deadline_dt = datetime.combine(datetime_now, deadline)
        time_now_dt = datetime.combine(datetime_now, time_now_obj)
        rem_time = deadline_dt - time_now_dt
    else:
        rem_time = None

    return rem_time

def sort_by_rem_time():
    todo_list.sort(key=lambda x: (x[1] is None, x[1]))

# MAIN PROGRAM LOOP
def main_loop():
    while True:
        print(todo_home())
        option = choose_option()
        if option == add_task:
            name = get_input("Enter task\n> ")
            option(name)
        else:
            option()
main_loop()