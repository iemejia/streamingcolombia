#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class CanalCapitalExtractor(StaticExtractor):

    NAME = u'Canal Capital'
    WEBPAGE_URL = 'http://www.canalcapital.gov.co/'
    LOGO_URL = 'http://www.canalcapital.gov.co/templates/canal_capital_2011/images/logo-navidad-2012.png'
    STREAMING_URL = 'http://livestream-f.akamaihd.net/i/4239881_2169976_f3c8e868_1@117636/master.m3u8?dw=100&__b__=446'
