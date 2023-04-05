#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for
a given employee ID, returns information about his/her TODO list progress.
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":

    response_user = requests.get('https://jsonplaceholder.typicode.com/users')
    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    user = response_user.json()
    todos = response_todos.json()

    for item in user:
        if str(item.get('id')) == str(sys.argv[1]):
            n = item.get('id')
            user_name = item.get('username')

    file = open(str(sys.argv[1]) + ".csv", 'w')
    csv_file = csv.writer(file, quoting=csv.QUOTE_ALL)
    for item in todos:
        li = []
        if str(item.get('userId')) == str(sys.argv[1]):
            li.append(n)
            li.append(user_name)
            task = item.get('completed')
            li.append(task)
            title = item.get('title')
            li.append(title)
            csv_file.writerow(li)
    file.close()
