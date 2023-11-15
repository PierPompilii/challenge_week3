
def track_my_tasks(text):
    if "TODO" in text:
        return "A task is pending"
    else:
        return "Task Done"