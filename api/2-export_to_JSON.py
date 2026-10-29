#!/usr/bin/python3
import json, requests, sys
if __name__ == "__main__":
    employee_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)).json()
    tasks = []
    for t in todos:
        tasks.append({"task": t.get("title"), "completed": t.get("completed"), "username": user.get("username")})
    with open("{}.json".format(employee_id), "w", encoding="utf-8") as f:
        json.dump({employee_id: tasks}, f)
