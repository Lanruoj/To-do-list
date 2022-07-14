from app import *

def test_exit_program(option):
    if option == "X":
        exit_program()

test_exit_program("X")