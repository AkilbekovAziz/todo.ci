MAX_TITLE_LENGTH = 50


def add_task(tasks, title):
    title = title.strip()
    if title == "" or len(title) > MAX_TITLE_LENGTH:
        return False
    tasks.append({"title": title, "done": False})
    return True


def delete_task(tasks, number):
    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        return removed["title"]
    return None


def mark_done(tasks, number):
    if 1 <= number <= len(tasks):
        tasks[number - 1]["done"] = True
        return True
    return False


def count_tasks(tasks):
    done = sum(1 for task in tasks if task["done"])
    return len(tasks), done


def set_priority(tasks, number, priority):
    if not 1 <= number <= len(tasks):
        return False
    if not 1 <= priority <= 3:
        return False
    tasks[number - 1]["priority"] = priority
    return True


PRIORITY_MARKS = {1: " (!!!)", 2: " (!!)", 3: " (!)"}


def format_task(number, task):
    if task["done"]:
        mark = "x"
    else:
        mark = " "
    priority = PRIORITY_MARKS.get(task.get("priority"), "")
    return f"{number}. [{mark}] {task['title']}{priority}"


def format_tasks(tasks):
    if len(tasks) == 0:
        return "Список пуст"
    lines = []
    for number, task in enumerate(tasks, start=1):
        lines.append(format_task(number, task))
    total, done = count_tasks(tasks)
    lines.append(f"Выполнено: {done} из {total}")
    return "\n".join(lines)
