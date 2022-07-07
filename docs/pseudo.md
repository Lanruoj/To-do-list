
* if first task of the day then show welcome message with morning/afternoon/evening
* global date/time?


## Home/todo list (todo_home)
* Receive sorted list from sort_list
- Displays:
- date/time
- remaining tasks (if any) sorted by deadline
- options for what the user can do
- Return todo_list

## Get user input (get_input)
* Receive prompt/message
- Ask user "prompt"
- Take user input, store as user_input
- Return user_input

## Choose option (choose_option)
- Take user input, store as option
- Options are:
1. Add task ("A")
2. Mark as done ("M")
3. Delete task ("D")
4. View completed tasks ("C")
5. Exit program ("X")
- Check which option user selects
- Return option

* ask repetitively??? ***********
## Get task (get_task)
- Take user input, store as task
	- check if valid input
- Return task

- **Store time added**
- Ask for deadline
	- check for valid input
	- store as deadline
- Return task

## Add task to list (add_task)
* Receive task from get_task
- Add task to unsorted_list (file or list)
- Return unsorted_list

## Sort list (sort_list)
* Receive unsorted list (unsorted_list)
- Sort list by deadline time (time remaining) *********
- Return todo_list

## Mark task as done (mark_as_done) *********** case insensitive?
* Receive todo_list, completed_list
- Ask user which task they'd like to mark as done, store as task
- Add task to *completed_list
- Remove task from todo_list
- Sort list
- Return todo_list

## Delete task (delete_task)
* Receive todo_list
- Ask "Which task the user would like to delete?", store response as task
- Remove task from todo_list
- Return todo_list

## View completed tasks (print_completed)
* Receive completed_list
- Format completed list in a presentable way
- Print completed_list

## Exit program
- Print goodbye message
- Break

Always return to home/todo list

