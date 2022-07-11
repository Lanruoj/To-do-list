from datetime import date, datetime, time, timedelta
from prettytable import PrettyTable

## GLOBAL VARIABLES ##
date_today = date.today()

datetime_now = datetime.now()

time_now_obj = datetime.now().time()

time_now_str = datetime.now().strftime("%H:%M:%S")

todo_list = []

## HOME ##
def todo_home():
    # todo_table = PrettyTable()
    # todo_table.field_names = ["Task", "Deadline", "Time remaining"]
    sort_by_remaining_time()
    print(f"Time: {time_now_str}")
    if todo_list == []:
        print("No current tasks")
    
    

    print(todo_list)
    print("Options:\n[A] Add a task\n[M] Mark as done\n[D] Delete a task\n[C] View completed list\n[X] Exit program")
    

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
    time_added_str = datetime.now().strftime(time_format)
    name = get_input("Enter task\n>")
    # has_deadline = get_input("Does this task have a deadline? [y/n]\n>")
    # deadline_input = ""
    # if has_deadline=="y":
        # while True: ### use a different condition!
    ## CHECK IF deadline_input MATCHES time_format ##
    while True:
        deadline_input = get_input("Enter deadline\n>")
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
                task = (name, time_added_str, deadline_obj, remaining_time)
                print(f"Remaining time: {remaining_time} minutes")
                todo_list.append(task)
                break

        except ValueError:
                print("ERROR: Invalid time format")
    

    # deadline_dt = datetime.combine(datetime_now, deadline_obj)
    # time_now_dt = datetime.combine(datetime_now, time_now_obj)
    # remaining_time = deadline_dt - time_now_dt
    # task = (name, time_added_str, deadline_obj, remaining_time)
    # print(f"Remaining time: {remaining_time} minutes")

    
    
    # print(f"Remaining time: {remaining_time} minutes")

    ## CREATE TASK OBJECT AS A TUPLE OF VALUES
    # task = (name, time_added_str, deadline_obj, remaining_time)
    ## ADD TASK TO GLOBAL LIST
    # todo_list.append(task)


## EXTRACT deadline FROM task TUPLE ##
def extract_remaining_time(task):
    return task[3] 

## SORT LIST BY DEADLINE TIME ##
def sort_by_remaining_time():
    todo_list.sort(key=extract_remaining_time)



def mark_as_done():
    pass

def delete_task():
    pass

def print_completed():
    pass

def exit_program():
    pass


## MAIN PROGRAM LOOP
def main_loop():
    while True:
        sort_by_remaining_time()
        todo_home()
        choose_option()

main_loop()