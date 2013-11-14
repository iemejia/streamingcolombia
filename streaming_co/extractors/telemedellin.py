#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class TeleMedellinExtractor(StaticExtractor):

    NAME = u'TeleMedellín'
    WEBPAGE_URL = 'http://www.telemedellin.tv/Paginas/senalenvivo.aspx'
    LOGO_URL = 'http://www.telemedellin.tv/images/static/logo.png'
    STREAMING_URL = 'http://api.new.livestream.com/broadcasts/34806153.m3u8?dw=100'
