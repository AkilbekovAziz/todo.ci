import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_todo_status_200():
    response = requests.get(f"{BASE_URL}/todos/1", timeout=10)
    assert response.status_code == 200


def test_get_todo_returns_json():
    response = requests.get(f"{BASE_URL}/todos/1", timeout=10)
    assert "application/json" in response.headers["Content-Type"]


def test_get_todo_fields():
    response = requests.get(f"{BASE_URL}/todos/1", timeout=10)
    data = response.json()
    assert data["id"] == 1
    assert data["userId"] == 1
    assert data["title"] == "delectus aut autem"
    assert data["completed"] == False


@pytest.mark.parametrize("todo_id", [0, 201, 9999])
def test_get_missing_todo_404(todo_id):
    response = requests.get(f"{BASE_URL}/todos/{todo_id}", timeout=10)
    assert response.status_code == 404


def test_filter_by_user():
    response = requests.get(f"{BASE_URL}/todos", params={"userId": 1}, timeout=10)
    data = response.json()
    assert len(data) == 20
    for item in data:
        assert item["userId"] == 1


def test_create_todo():
    new_todo = {"title": "Сдать лабу", "completed": False, "userId": 1}
    response = requests.post(f"{BASE_URL}/todos", json=new_todo, timeout=10)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Сдать лабу"
    assert data["id"] == 201
