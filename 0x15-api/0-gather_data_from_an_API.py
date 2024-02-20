#!/usr/bin/python3

""""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import urllib.request
import json
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    with urllib.request.urlopen(url + sys.argv[1]) as response:
        data = json.loads(response.read().decode("utf-8"))
        name = data.get('name')
    url = "https://jsonplaceholder.typicode.com/todos?userId="
    with urllib.request.urlopen(url + sys.argv[1]) as response:
        data = json.loads(response.read().decode("utf-8"))
        done = [task for task in data if task.get('completed')]
        print("Employee {} is done with tasks({}/{}):".format(
           name, len(done), len(data)))
    [print("\t {}".format(task.get('title'))) for task in done]
