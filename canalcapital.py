#!/usr/local/bin/env python

from __future__ import print_function
import requests
import json
from xml.dom import minidom
# import pprint

CANALCAPITAL_ACCOUNT_ID = '4239881'
CANALCAPITAL_EVENT_ID = '2169976'

LIVESTREAM_API_URL = 'http://new.livestream.com/api/'


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


def get_video_info(account_id, event_id):
    url = LIVESTREAM_API_URL + \
        'accounts/%s/events/%s/viewing_info' % (account_id, event_id)
    return query(url)


def get_video_smil(account_id, event_id):
    res = get_video_info(account_id, event_id)
    val = json.loads(res)
    # pprint.pprint(val)
    return val['streamInfo']['play_url']


def get_streaming_url_from_smil(smil):
    xml = minidom.parseString(smil)
    itemlist = xml.getElementsByTagName('meta')
    http_base = ''
    for item in itemlist:
        if item.attributes['name'].value == 'httpBase':
            http_base = item.attributes['content'].value
    video = xml.getElementsByTagName('video')
    video_path = video[0].attributes['src'].value
    streaming_url = http_base + video_path
    return streaming_url

if __name__ == "__main__":
    smil_url = get_video_smil(CANALCAPITAL_ACCOUNT_ID, CANALCAPITAL_EVENT_ID)
    smil = query(smil_url)
    print(get_streaming_url_from_smil(smil))
