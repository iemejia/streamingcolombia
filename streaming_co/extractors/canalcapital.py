#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from .livestreamextractor import LiveStreamExtractor

class CanalCapitalExtractor(LiveStreamExtractor):

    NAME = u'Canal Capital'
    WEBPAGE_URL = 'http://www.canalcapital.gov.co/'
    LOGO_URL = 'http://www.canalcapital.gov.co/templates/canal_capital_2011/images/logo-navidad-2012.png'
    account_id = '4239881'
    event_id = '2169976'
    LIVESTREAMER_URL = 'http://new.livestream.com/accounts/4239881/events/2169976/'
    IS_PLAYABLE = False
