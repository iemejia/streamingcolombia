# -*- coding: utf-8 -*-

from __future__ import print_function

from .staticextractor import StaticExtractor

class TeleMedellinExtractor(StaticExtractor):

    NAME = u'TeleMedellín'
    WEBPAGE_URL = 'http://www.telemedellin.tv/Paginas/senalenvivo.aspx'
    LOGO_URL = 'http://www.telemedellin.tv/images/static/logo.png'
    LIVESTREAMER_URL = 'http://new.livestream.com/accounts/4608897/events/2230380/'
