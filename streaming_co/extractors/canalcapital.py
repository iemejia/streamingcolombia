# -*- coding: utf-8 -*-

from __future__ import print_function

from .staticextractor import StaticExtractor

class CanalCapitalExtractor(StaticExtractor):

    NAME = u'Canal Capital'
    WEBPAGE_URL = 'http://www.canalcapital.gov.co/'
    LOGO_URL = 'http://www.canalcapital.gov.co/templates/canal_capital_2011/images/logo-navidad-2012.png'
    LIVESTREAMER_URL = 'hds://http://cdns840stu1010.multistream.net/canalcapitallive/amlst:live/manifest.f4m'
