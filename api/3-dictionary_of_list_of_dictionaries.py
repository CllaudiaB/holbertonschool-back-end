#!/usr/bin/python3
"""
    script to export data in the JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":
    response_user = requests.get("https://jsonplaceholder.typicode.com/users")
    user = response_user.json()
    response_todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = response_todos.json()

    _dict1 = {}

    for item in user:
        n = item.get('id')
        user_name = item.get('username')
        li = []
        for other_item in todos:
            if other_item.get('userId') == n:
                _dict = {}
                _dict['username'] = user_name
                _dict['task'] = other_item.get('title')
                _dict['completed'] = other_item.get('completed')
                li.append(_dict)
        _dict1[n] = li

    json_dict = json.dumps(_dict1)
    with open("todo_all_employees.json", "w") as file:
        file.write(json_dict)
