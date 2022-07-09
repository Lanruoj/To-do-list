# Pseudocode

* if first task of the day then show welcome message with morning/afternoon/evening
* global date/time?


## Home/todo list (todo_home)
* Receive unsorted_list
- If any tasks to do:
	- Sort unsorted_list, as sorted_list
	- Displays:
		- date/time (date_time)
		- remaining tasks (if any) sorted by deadline (todo_list)
		- options for what the user can do
- If not, put "No tasks yet" in the display
- Return display


## Get user input (get_input)
* Receive prompt/message
- Ask user "prompt"
- Take user input, store as user_input
- Return user_input


## Choose option (get_option)
- Take user input, store as option
- Options are: *DICT*
1. Add task ("A")
2. Mark as done ("M")
3. Delete task ("D")
4. View completed tasks ("C")
5. Exit program ("X")
- Check if input is a valid option in the dictionary, if not:
	- print error message
	- repeat function
- Return option


## Add task (add_task)
- Take user input, store as task
- **Store time added**
- Ask for deadline
- check for valid input
- if "yes":
    - take user input, store as choice
    - if input valid time format:	
    - store as deadline
- otherwise skip
- Add task to unsorted_list


## Sort list (sort_list)
* Receive unsorted list (unsorted_list)
- Sort list by deadline time (time remaining) *********
- Return todo_list


## Mark task as done (mark_as_done)
* Receive sorted_list, completed_list
- Ask user which task they'd like to mark as done, store as task
- if task is in list:
	- remove from sorted_list
	- Add task to *completed_list
	- Remove task from sorted_list
	- Return "<task> marked as complete"
- otherwise:
	- print "item is not in list"
	- repeat input
-----> completed list is global var


## Delete task (delete_task)
- Ask "Which task would you like to delete?", store response as task
- if task is in sorted_list:
	- remove task from sorted_list
	- return "<task> deleted"
- otherwise:
	- print "item is not in list"
	- repeat input


## View completed tasks (print_completed)
- Format completed list in a presentable way
- Print completed_list


## Exit program
- Print goodbye message
- Break


* Always return to home/todo list



## FUNCTION LIST
- todo_home(unsorted_list)

- get_input(prompt)

- choose_option()

- add_task(task)

- sort_list(unsorted_list)

- mark_as_done(todo_list, completed_list)

- delete_task(todo_list)

- print_completed(completed_list)

- exit_program()