# *T1A3 Terminal App assessment* - Tane Kaio, 2022

## Source control
[Github repository](https://github.com/Lanruoj/To-do-list/tree/master)

## Implementation plan
[Trello board](https://trello.com/b/5F9d2hi9/t1a3-terminal-application)

## Flowcharts


## Style guide  
I will be following the [Python Enhancement Proposals 8](https://peps.python.org/pep-0008/) (Pep8). 

## Concept:
*To-do list app*
First, it greets the user with the day/date/time and displays that day's tasks in the format of a to-do list sorted by deadline times (unless the list is empty). Then, users can:
* Choose an option for what to do
* Add a task from user input
* Store time task was added
* Store optional deadline with task
* Mark tasks as done
* Delete tasks
* View completed tasks
* Gracefully quit program

## List of features:
1. Display todo-list with a formatted string in a table-like design
    - Uses datetime module for time and date information/calculations
    - "Home" function, all functions except exit loops back to this
    - Sorts the global unsorted list on each execution
    - Displays task name, time added, deadline time, and time remaining (using timedelta)
    - Takes in the tasks from a global data structure
    - If no tasks, show "no current tasks"
    - Show options for user

2. User can choose an option for what to do 
    - Checks for keyboard input that matches a dictionary of options (local variable)
        - If it doesn't, throw error and try again
    - Runs the corresponding function name as the value in dictionary

3. Add a task to the todo-list with time information
    - Asks for user to add a task
    - Stores time added with task object (using datetime module)
    - Asks user if the task has a deadline/due-date
        - If the time isn't in the specified format, throw an error and ask again
    - If it does, stores deadline with the task object
    - Adds task to global unsorted list

4. Mark tasks as done
    - User can mark a task as completed 
    - Checks if task is in list or not
        - If it doesn't, throw error and try again
    - Otherwise, adds it to a global completed list
    - Removes from global todo list



## Tests
1. Check that `choose_options()` outputs and runs a function when user input matches option
    * Run a dummy function `print_hello` that prints `"hello"` when user inputs corresponding dictionary key `"H"`
    
