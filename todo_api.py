import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def api_to_task(data):
    return {"title": data["title"], "done": data["completed"]}


def fetch_todo(todo_id):
    response = requests.get(f"{BASE_URL}/todos/{todo_id}", timeout=TIMEOUT)
    if response.status_code == 404:
        return None
    return api_to_task(response.json())


def fetch_user_todos(user_id):
    response = requests.get(f"{BASE_URL}/todos", params={"userId": user_id}, timeout=TIMEOUT)
    tasks = []
    for item in response.json():
        tasks.append(api_to_task(item))
    return tasks
