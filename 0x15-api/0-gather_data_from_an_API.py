#!/usr/bin/python3

""""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
import sys

if __name__ == "__main__":
   url = "https://jsonplaceholder.typicode.com/"
   emp_name = requests.get(url + "users/{}".format(sys.argv[1])).json()
   done_tasks = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
   completed = [t.get("title") for t in done_tasks if t.get("completed") is True]
   
   print("Employee {} is done with tasks({}/{}):".format(emp_name.get("name"),
                                                         len(completed),
                                                         len(done_tasks)))
   [print("\t {}".format(task)) for task in completed]