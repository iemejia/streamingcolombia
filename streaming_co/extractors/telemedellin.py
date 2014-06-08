#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from .livestreamextractor import LiveStreamExtractor

class TeleMedellinExtractor(LiveStreamExtractor):

    NAME = u'TeleMedellín'
    WEBPAGE_URL = 'http://www.telemedellin.tv/Paginas/senalenvivo.aspx'
    LOGO_URL = 'http://www.telemedellin.tv/images/static/logo.png'
    account_id = '4608897'
    event_id = '2230380'
    IS_PLAYABLE = False
