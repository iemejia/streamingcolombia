#!/usr/local/bin/env python

from __future__ import print_function

import json
# import pprint

from .extractor import Extractor
from utils import *
from xml.dom import minidom

class CanalCapitalExtractor(Extractor):

    NAME = 'Canal Capital'
    WEBPAGE_URL = 'http://www.canalcapital.gov.co/'

    CANALCAPITAL_ACCOUNT_ID = '4239881'
    CANALCAPITAL_EVENT_ID = '2169976'

    LIVESTREAM_API_URL = 'http://new.livestream.com/api/'

    def get_video_info(self,account_id, event_id):
        url = self.LIVESTREAM_API_URL + \
            'accounts/%s/events/%s/viewing_info' % (account_id, event_id)
        return query(url)


    def get_video_smil(self,account_id, event_id):
        res = self.get_video_info(account_id, event_id)
        val = json.loads(res)
        # pprint.pprint(val)
        return val['streamInfo']['play_url']


    def get_streaming_url_from_smil(self,smil):
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

    def extract(self):
        smil_url = self.get_video_smil(self.CANALCAPITAL_ACCOUNT_ID,
                                       self.CANALCAPITAL_EVENT_ID)
        smil = query(smil_url)
        return self.get_streaming_url_from_smil(smil)

if __name__ == "__main__":
    e = CanalCapitalExtractor()
    print(e.extract())
