from todo_logic import add_task, delete_task, mark_done, count_tasks


def test_add_task_adds_to_list():
    tasks = []
    result = add_task(tasks, "Купить хлеб")
    assert result == True
    assert tasks == [{"title": "Купить хлеб", "done": False}]


def test_add_task_strips_spaces():
    tasks = []
    add_task(tasks, "  Позвонить маме  ")
    assert tasks[0]["title"] == "Позвонить маме"


def test_add_task_rejects_empty_title():
    tasks = []
    assert add_task(tasks, "   ") == False
    assert tasks == []


def test_delete_task_removes_by_number():
    tasks = []
    add_task(tasks, "Первая")
    add_task(tasks, "Вторая")
    assert delete_task(tasks, 1) == "Первая"
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Вторая"


def test_delete_task_wrong_number():
    tasks = []
    add_task(tasks, "Единственная")
    assert delete_task(tasks, 0) is None
    assert delete_task(tasks, 5) is None
    assert len(tasks) == 1


def test_mark_done():
    tasks = []
    add_task(tasks, "Сделать ДЗ")
    assert mark_done(tasks, 1) == True
    assert tasks[0]["done"] == True


def test_count_tasks_empty():
    assert count_tasks([]) == (0, 0)


def test_count_tasks_with_done():
    tasks = []
    add_task(tasks, "A")
    add_task(tasks, "B")
    add_task(tasks, "C")
    mark_done(tasks, 2)
    assert count_tasks(tasks) == (3, 1)
