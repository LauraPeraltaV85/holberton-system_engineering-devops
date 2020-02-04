#!/usr/bin/python3
"""
dictionary of list of dictionaries
"""
if __name__ == "__main__":
    import json
    import requests
    req_user = requests.get('https://jsonplaceholder.typicode.com/users')
    ttask = requests.get('https://jsonplaceholder.typicode.com/todos')
    tot_n_tasks = ttask.json()
    dict_dict = {}
    for names in req_user.json():
        em_name = names.get('username')
        ids = names.get('id')
        dict_list = []

        for task in tot_n_tasks:
            if (task.get('userId') == ids and task.get("completed")):
                t_tasks = {}
                t_tasks['task'] = task.get('title')
                t_tasks['completed'] = task.get('completed')
                t_tasks['username'] = em_name

                # t_tasks = {'task': task.get('title'),
                #           'completed': task.get('completed'),
                #           'username': em_name}
                dict_list.append(t_tasks)

        dict_dict[ids] = dict_list

    with open('todo_all_employees.json', 'w', encoding="utf-8") as file:
        json.dump(dict_dict, file)
