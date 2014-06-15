#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class TuKanalExtractor(StaticExtractor):

    NAME = u'Tu Kanal'
    WEBPAGE_URL = 'http://www.tukanal.tv/images/'
    LOGO_URL = 'http://www.tukanal.tv/images/logo2.png'
    STREAMING_URL = 'http://www.ustream.tv/channel/tukanalchannel'
    LIVESTREAMER_URL = 'http://www.ustream.tv/channel/tukanalchannel'
    IS_PLAYABLE = False
