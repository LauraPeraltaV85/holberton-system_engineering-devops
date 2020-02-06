#!/usr/bin/python3
"""
gather data from API
"""
import requests


def number_of_subscribers(subreddit):
    headers = {'user-agent': 'laura_req'}
    subreddits_ = requests.get("https://www.reddit.com/r/{}/about.json"
                               .format(subreddit), headers=headers)
    if subreddits_.status_code is 200:
        subscribers = (subreddits_.json().get('data').get('subscribers'))
        return subscribers
    else:
        return 0
