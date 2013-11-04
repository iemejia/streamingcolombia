#!/usr/local/bin/env python

from __future__ import print_function

from .livestreamextractor import LiveStreamExtractor

class TeleMedellinExtractor(LiveStreamExtractor):

    NAME = 'TeleMedellín'
    WEBPAGE_URL = 'http://www.telemedellin.tv/Paginas/senalenvivo.aspx'

    account_id = '4608897'
    event_id = '2230380'

if __name__ == "__main__":
    e = TeleMedellinExtractor()
    print(e.extract())