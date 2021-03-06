#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class TeleAmigaExtractor(StaticExtractor):

    NAME = u'TeleAmiga'
    WEBPAGE_URL = 'http://www.teleamiga.tv/'
    LOGO_URL = 'http://www.teleamiga.tv/templates/tr_neutrino/images/logos/logo.png'
    # STREAMING_URL = 'mms://208.109.243.17:8081/teleamiga'
