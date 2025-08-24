def add_task(task_list, task_name):
    task = {"name": task_name, "completed": False}
    return task_list + [task]

def list_pending(task_list):
    return list(filter(lambda t: not t["completed"], task_list))

def complete_all(task_list):
    return list(map(lambda t: {**t, "completed": True}, task_list))

def search_tasks(task_list, keyword):
    return list(filter(lambda t: keyword.lower() in t["name"].lower(), task_list))

tasks = []
tasks = add_task(tasks, "Buy groceries")
tasks = add_task(tasks, "Finish assignment")
tasks = add_task(tasks, "Call friend")

print("Pending Tasks:", list_pending(tasks))

tasks = complete_all(tasks)
print("All tasks after marking complete:", tasks)

print("Search Result for 'call':", search_tasks(tasks, "call"))