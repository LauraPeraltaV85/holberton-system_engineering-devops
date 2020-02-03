#!/usr/bin/python3
"""
export to CSV
"""
if __name__ == "__main__":
    import csv
    import requests
    from sys import argv
    req_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(argv[1]))
    em_name = (req_user.json().get('username'))
    ttask = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(argv[1]))
    tot_n_tasks = ttask.json()
    with open('{}.csv'.format(argv[1]), mode='w') as csv_file:
        csv = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in tot_n_tasks:
            csv.writerow([task.get('userId'), em_name,
                          task.get('completed'), task.get('title')])
