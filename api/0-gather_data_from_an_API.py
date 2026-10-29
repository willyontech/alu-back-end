#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    user_data = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id)).json()
    todos_data = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)).json()
    done = [t for t in todos_data if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(user_data.get("name"), len(done), len(todos_data)))
    for task in done:
        print("\t {}".format(task.get("title")))
