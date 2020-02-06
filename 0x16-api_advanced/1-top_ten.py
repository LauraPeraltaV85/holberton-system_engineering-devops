#!/usr/bin/python3
"""
top 10 posts
"""
import requests


def top_ten(subreddit):
    headers = {'user-agent': 'laura_req'}
    subredts_ = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                             .format(subreddit), headers=headers)
    if subredts_.status_code is 200:
        subscribers = (subredts_.json().get('data').get('children'))
        for hot in subscribers:
            print(hot.get('data').get('title'))
    else:
        print(None)
