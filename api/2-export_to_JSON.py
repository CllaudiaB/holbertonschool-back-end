#!/usr/bin/python3
"""
    script to export data in the JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    response_user = requests.get("https://jsonplaceholder.typicode.com/users")
    response_todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    user = response_user.json()
    todos = response_todos.json()

    for item in user:
        if int(sys.argv[1]) == item.get('id'):
            n = item.get('id')
            user_name = item.get('username')

    li = []

    for item in todos:
        _dict = {}
        if int(sys.argv[1]) == item.get('userId'):
            _dict['task'] = item.get('title')
            _dict['completed'] = item.get('completed')
            _dict1['username'] = user_name
            li.append(_dict)

    _dict1 = {}
    _dict1[n] = li

    json_dict = json.dumps(_dict1)
    with open(str(argv[1]) + ".json", "w") as file:
        file.write(json_dict)
