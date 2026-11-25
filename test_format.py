from todo_logic import add_task, mark_done, set_priority, format_tasks


def test_format_empty_list():
    assert format_tasks([]) == "Список пуст"


def test_format_one_task():
    tasks = []
    add_task(tasks, "Купить хлеб")
    assert format_tasks(tasks) == "1. [ ] Купить хлеб\nВыполнено: 0 из 1"


def test_format_done_task():
    tasks = []
    add_task(tasks, "Купить хлеб")
    add_task(tasks, "Сделать ДЗ")
    mark_done(tasks, 2)
    assert format_tasks(tasks) == (
        "1. [ ] Купить хлеб\n"
        "2. [x] Сделать ДЗ\n"
        "Выполнено: 1 из 2"
    )


def test_format_priorities():
    tasks = []
    add_task(tasks, "A")
    add_task(tasks, "B")
    add_task(tasks, "C")
    set_priority(tasks, 1, 1)
    set_priority(tasks, 2, 2)
    set_priority(tasks, 3, 3)
    assert format_tasks(tasks) == (
        "1. [ ] A (!!!)\n"
        "2. [ ] B (!!)\n"
        "3. [ ] C (!)\n"
        "Выполнено: 0 из 3"
    )


def test_format_task_without_priority():
    tasks = []
    add_task(tasks, "A")
    add_task(tasks, "B")
    set_priority(tasks, 2, 1)
    assert format_tasks(tasks).splitlines()[0] == "1. [ ] A"
