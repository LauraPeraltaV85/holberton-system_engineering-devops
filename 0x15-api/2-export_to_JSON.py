#!/usr/bin/python3
"""
export to json
"""
if __name__ == "__main__":
    import json
    import requests
    from sys import argv
    req_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(argv[1]))
    em_name = (req_user.json().get('username'))
    ttask = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(argv[1]))
    tot_n_tasks = ttask.json()
    dict_list = []
    for task in tot_n_tasks:
        t_tasks = {'task': task.get('title'),
                   'completed': task.get('completed'), 'username': em_name}
        dict_list.append(t_tasks)
    dict_user = {argv[1]: dict_list}
    with open('{}.json'.format(argv[1]), 'w', encoding="utf-8") as file:
        json.dump(dict_user, file)
