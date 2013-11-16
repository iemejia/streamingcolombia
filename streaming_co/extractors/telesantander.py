#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class TeleSantanderExtractor(StaticExtractor):

    NAME = u'Tele Santander'
    WEBPAGE_URL = 'http://www.telesantander.com/'
    LOGO_URL = 'http://www.telesantander.com/templates/rt_solarsentinel_j15/images/header/green/logo.png'
    STREAMING_URL = 'rtmp://wow.eleden.com:1935/livesantander/livestream'
