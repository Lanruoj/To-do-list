from app import extract_deadline, add_task, todo_list

# TEST SORTING BY DEADLINE WORKS -----------------------
def test_sort_by_deadline():
    while True:
        add_task()
        print(f"Unsorted list: {todo_list}")
        todo_list.sort(key=extract_deadline)
        print(f"Sorted list: {todo_list}")

test_sort_by_deadline()