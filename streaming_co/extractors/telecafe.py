#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class TeleCafeExtractor(StaticExtractor):

    NAME = u'Telecafé'
    WEBPAGE_URL = 'http://telecafe.gov.co/en/'
    LOGO_URL = 'http://telecafe.gov.co/wp-content/uploads/2013/11/logo-telecafe-2013.png'
    STREAMING_URL = 'http://xtelecafex.api.channel.livestream.com/3.0/playlist.m3u8'
