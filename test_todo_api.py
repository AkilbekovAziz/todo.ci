from todo_api import api_to_task, fetch_todo, fetch_user_todos
from todo_logic import format_tasks


# Без интернета: проверяем только перевод данных API в нашу задачу

def test_api_to_task_not_done():
    data = {"userId": 1, "id": 1, "title": "Купить хлеб", "completed": False}
    assert api_to_task(data) == {"title": "Купить хлеб", "done": False}


def test_api_to_task_done():
    data = {"userId": 1, "id": 4, "title": "Сделать ДЗ", "completed": True}
    assert api_to_task(data) == {"title": "Сделать ДЗ", "done": True}


def test_api_task_works_with_format_tasks():
    data = {"userId": 1, "id": 1, "title": "Купить хлеб", "completed": True}
    tasks = [api_to_task(data)]
    assert format_tasks(tasks) == "1. [x] Купить хлеб\nВыполнено: 1 из 1"


# С интернетом: настоящий запрос к API

def test_fetch_todo():
    assert fetch_todo(1) == {"title": "delectus aut autem", "done": False}


def test_fetch_missing_todo():
    assert fetch_todo(9999) is None


def test_fetch_user_todos():
    tasks = fetch_user_todos(1)
    assert len(tasks) == 20
    assert tasks[0] == {"title": "delectus aut autem", "done": False}
