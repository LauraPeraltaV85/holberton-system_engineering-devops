#!/usr/bin/python3
"""
hot post reursively
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    headers = {'user-agent': 'laura_req'}
    if (len(hot_list) == 0):
        subr = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit), headers=headers)
    else:
        subr = requests.get("https://www.reddit.com/r/{}/hot.json?after={}"
                            .format(subreddit, after), headers=headers)

    if subr.status_code is 200:
        subscribers = (subr.json().get('data').get('children'))
        for hot in subscribers:
            hot_list.append(hot.get('data').get('title'))
    else:
        return(None)
    after = (subr.json().get('data').get('after'))
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
