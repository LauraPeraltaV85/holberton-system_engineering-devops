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
    dict_list = []
    user_id_1 = tot_n_tasks.get('user_id')
    for task in tot_n_tasks:
        user_id = task.get('userId')
        for names in req_user.json():
            em_name = names.get('username')
            if user_id is names.get('id'):
                t_tasks = {'task': task.get('title'),
                           'completed': task.get('completed'), 'username': em_name}
                dict_list.append(t_tasks)
        if :
        dict_user = {user_id: dict_list}
    print(dict_list)
    with open('todo_all_employees.json', 'w', encoding="utf-8") as file:
        json.dump(dict_user, file)
