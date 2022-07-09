## GLOBAL VARIABLES

def get_input(prompt):
    user_input = input(prompt)
    return user_input

def choose_option():
    options = {
        "A": add_task,
        "M": mark_as_done,
        "D": delete_task,
        "C": print_completed,
        "X": exit_program
    }
    while True:
        option = get_input("> ")
        if option not in options:
            print("Invalid option")
        else:
            return options[option]()

######

def add_task():
    task = get_input("Enter task > ")
    




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