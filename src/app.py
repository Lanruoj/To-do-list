from datetime import date, datetime, time, timedelta
from prettytable import PrettyTable

## GLOBAL VARIABLES ##
date_today = date.today()
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
            return options[option]()


## ADD TASK TO LIST ##
def add_task():
    datetime_now = datetime.now()
    time_now_obj = datetime.now().time()
    time_added_str = datetime.now().strftime(time_format)
    name = get_input("Enter task\n> ")

    # has_deadline = get_input("Does this task have a deadline? [y/n]\n>")
    # if has_deadline == "y":

        ## CHECK IF deadline_input MATCHES time_format ##
    while True:
        deadline_input = get_input("Enter deadline\n> ")
        try: 
            datetime_now = datetime.now()
            deadline_obj = datetime.strptime(deadline_input, time_format).time()
            # deadline_str = datetime.strftime(deadline_input, time_format)
            if deadline_obj < time_now_obj:
                print("ERROR: Time must be in the future")               
            else:
                deadline_dt = datetime.combine(datetime_now, deadline_obj)
                time_now_dt = datetime.combine(datetime_now, time_now_obj)
                remaining_time = deadline_dt - time_now_dt
                break
        except ValueError:
                print("ERROR: Invalid time format")

    task = (name, time_added_str, deadline_obj, remaining_time)
    todo_list.append(task)


## EXTRACT deadline FROM task TUPLE ##
def extract_remaining_time(item):
    return item[3] 


## SORT LIST BY DEADLINE TIME ##
def sort_by_remaining_time():
    todo_list.sort(key=extract_remaining_time)


def mark_as_done():
    task = get_input("Enter completed task\n> ")
    # while True:
    for i in todo_list:
        if task == i[0]:
            time_added_str = datetime.now().strftime(time_format)
            completed_task = (i[0], time_added_str)
            completed_list.append(completed_task)
            todo_list.remove(i)
            break
    else:
        print("ERROR: No existing task")
    
    return completed_list


def delete_task():
    task = get_input("Enter completed task\n> ")
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
    option = get_input("Continue? [y/n]\n> ")
    if option == "y":
        todo_home()


## HOME ##
def todo_home():
    time_now_str = datetime.now().strftime(time_format)
    sort_by_remaining_time()
    todo_table = PrettyTable()
    todo_table.field_names = ["Task", "Deadline", "Time remaining"]

    if len(todo_list) < 1:
        todo_table.add_row(["No current tasks", "-", "-"])    
    else:
        for task in todo_list:       
            todo_table.add_row([task[0], task[2], task[3]])

    home_display = f"Time: {time_now_str}\n{todo_table}\nOptions:\n[A] Add a task\n[M] Mark as done\n[D] Delete a task\n[C] View completed list\n[X] Exit program"
    return home_display
    

# def exit_program():
#     confirmation = input("Are you sure you want to quit? [y/n]\n> ")
#     if confirmation == "y":
#         quit()
#     else:
#         return False

## MAIN PROGRAM LOOP
def main_loop():
    while True:
        sort_by_remaining_time()
        print(todo_home())
        choose_option()

main_loop()