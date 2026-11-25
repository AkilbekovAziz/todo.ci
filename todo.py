from todo_logic import add_task, delete_task, mark_done, count_tasks, set_priority, format_tasks
from todo_api import fetch_user_todos


def ask_number(prompt):
    answer = input(prompt).strip()
    if answer.isdigit():
        return int(answer)
    return None


tasks = []

print("Список задач. Команды: add, show, done, delete, priority, count, import, exit")

while True:
    command = input("> ").strip()

    if command == "add":
        title = input("Задача: ")
        if add_task(tasks, title):
            print("Добавлено!")
        else:
            print("Название пустое или длиннее 50 символов")
    elif command == "show":
        print(format_tasks(tasks))
    elif command == "done":
        number = ask_number("Номер задачи: ")
        if number is not None and mark_done(tasks, number):
            print("Отмечено!")
        else:
            print("Нет задачи с таким номером")
    elif command == "delete":
        number = ask_number("Номер задачи: ")
        removed = delete_task(tasks, number) if number is not None else None
        if removed is None:
            print("Нет задачи с таким номером")
        else:
            print(f"Удалено: {removed}")
    elif command == "priority":
        number = ask_number("Номер задачи: ")
        priority = ask_number("Приоритет (1–3): ")
        if number is not None and priority is not None and set_priority(tasks, number, priority):
            print("Приоритет установлен!")
        else:
            print("Неверный номер или приоритет")
    elif command == "count":
        total, done = count_tasks(tasks)
        print(f"Всего задач: {total}, выполнено: {done}")
    elif command == "import":
        user_id = ask_number("Номер пользователя (1–10): ")
        if user_id is None:
            print("Нужно число")
        else:
            new_tasks = fetch_user_todos(user_id)
            tasks.extend(new_tasks)
            print(f"Загружено задач: {len(new_tasks)}")
    elif command == "exit":
        print("Пока!")
        break
    else:
        print("Неизвестная команда")
