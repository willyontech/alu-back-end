#!/usr/bin/python3
import csv, requests, sys
if __name__ == "__main__":
    employee_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)).json()
    with open("{}.csv".format(employee_id), "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([employee_id, user.get("username"), t.get("completed"), t.get("title")])
