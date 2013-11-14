#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from .livestreamextractor import LiveStreamExtractor

class TeleMedellinExtractor(LiveStreamExtractor):

    NAME = u'TeleMedellín'
    WEBPAGE_URL = 'http://www.telemedellin.tv/Paginas/senalenvivo.aspx'

    account_id = '4608897'
    event_id = '2230380'
