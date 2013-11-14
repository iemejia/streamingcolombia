#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class SenalColombiaExtractor(StaticExtractor):

    NAME = u'Señal Colombia'
    WEBPAGE_URL = 'http://www.senalcolombia.tv/player/popupsc/'
    LOGO_URL = 'http://www.senalcolombia.tv/templates/senalcolombia-2013/images/sc/header3/logo_senalcol.png'
    STREAMING_URL = 'rtmp://cdns724ste1010.multistream.net/rtvc2live/live-500'
