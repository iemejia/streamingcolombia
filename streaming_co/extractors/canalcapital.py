#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from .livestreamextractor import LiveStreamExtractor

class CanalCapitalExtractor(LiveStreamExtractor):

    NAME = u'Canal Capital'
    WEBPAGE_URL = 'http://www.canalcapital.gov.co/'

    account_id = '4239881'
    event_id = '2169976'

if __name__ == "__main__":
    e = CanalCapitalExtractor()
    print(e.extract())
