#!/usr/bin/python3
"""
gather data from API
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    req_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(argv[1]))
    em_name = (req_user.json().get('name'))
    ttask = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(argv[1]))
    tot_n_tasks = ttask.json()
    tot_n_tasks_len = len(tot_n_tasks)
    i = 0
    titles = []
    for task in tot_n_tasks:
        tot_n_tasks_done = task.get('completed')
        if tot_n_tasks_done is True:
            titles.append(task.get('title'))
            i = i + 1
    print("Employee {} is done with tasks({}/{}):".format(em_name, i,
                                                          tot_n_tasks_len))
    for title in titles:
        print("\t {}".format(title))
