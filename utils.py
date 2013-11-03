#!/usr/local/bin/env python

import requests

def query(url, params=None, headers=None):
    # headers = {'Authorization': TOKEN}
    r = requests.get(url, params=params, headers=headers)
    if r.status_code != 200:
        if r.status_code == 429:
            print('too many requests')
        if r.status_code == 401:
            print('invalid token')
        else:
            print('error querying the API (%s)' % r.status_code)
            print(r.url)
    return r.text
