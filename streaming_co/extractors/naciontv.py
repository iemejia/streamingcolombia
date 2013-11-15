#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class NacionTVExtractor(StaticExtractor):

    NAME = u'Nación TV'
    WEBPAGE_URL = 'http://www.naciontv.co/al_aire.html'
    LOGO_URL = 'http://www.naciontv.co/_interfAz_CK!/naciontv.png'
    STREAMING_URL = ''
    IS_PLAYABLE = False
