import pytest
from todo_logic import add_task, delete_task, set_priority


def make_tasks(count):
    tasks = []
    for i in range(count):
        add_task(tasks, f"Задача {i + 1}")
    return tasks


@pytest.mark.parametrize("title, expected", [
    ("", False),          # пустая строка
    ("   ", False),       # одни пробелы
    ("a", True),          # 1 символ — нижняя граница
    ("a" * 50, True),     # 50 символов — верхняя граница
    ("a" * 51, False),    # 51 символ — сразу за границей
])
def test_add_task_title_length(title, expected):
    tasks = []
    assert add_task(tasks, title) == expected


@pytest.mark.parametrize("priority, expected", [
    (0, False),   # сразу ниже границы
    (1, True),    # нижняя граница
    (2, True),    # середина
    (3, True),    # верхняя граница
    (4, False),   # сразу выше границы
    (-5, False),  # отрицательное число
])
def test_set_priority_values(priority, expected):
    tasks = make_tasks(1)
    assert set_priority(tasks, 1, priority) == expected


@pytest.mark.parametrize("number, expected", [
    (0, None),           # ниже границы
    (1, "Задача 1"),     # первая задача
    (3, "Задача 3"),     # последняя задача
    (4, None),           # за концом списка
])
def test_delete_task_numbers(number, expected):
    tasks = make_tasks(3)
    assert delete_task(tasks, number) == expected


def test_set_priority_wrong_number():
    tasks = make_tasks(2)
    assert set_priority(tasks, 3, 1) == False
    assert "priority" not in tasks[0]
