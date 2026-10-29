#!/usr/bin/python3
import json, requests
if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    usernames = {u["id"]: u["username"] for u in users}
    data = {str(u["id"]): [] for u in users}
    for t in todos:
        data[str(t["userId"])].append({"username": usernames[t["userId"]], "task": t["title"], "completed": t["completed"]})
    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        json.dump(data, f)
