#!/usr/bin/python3
from datadog import initialize, api

options = {
    'api_key': '9477b8a172e4b80ac1dba7ebbdee37d6',
    'app_key': 'd75b0b1bcd94b3734240241d631c2d04375b26fb'
}

initialize(**options)

print(api.Dashboard.get_all())
