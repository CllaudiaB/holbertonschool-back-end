#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data
in the JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":

    response_user = requests.get('https://jsonplaceholder.typicode.com/users')
    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    user = response_user.json()
    todos = response_todos.json()


    for item in user:
        if str(sys.argv[1]) == str(item.get('id')):
            n = item.get('id')
            user_name = item.get('username')

    li = []
    for item in todos:
        _dict = {}
        if str(sys.argv[1]) == str(item.get('userId')):
            title = item.get('title')
            task = item.get('completed')
            _dict['title'] = title
            _dict['completed'] = task
            _dict['username'] = user_name
            li.append(_dict)

    _dict1 = {}
    _dict1[str(sys.argv[1])] = li
    with open(str(sys.argv[1]) + ".json", "w") as file:
        json.dump(_dict1, file)
