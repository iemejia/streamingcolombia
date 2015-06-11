#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class CanalUExtractor(StaticExtractor):

    NAME = u'Canal U'
    WEBPAGE_URL = 'http://www.canalu.com.co/senal-envivo'
    LOGO_URL = 'http://www.canalu.com.co/img/logo-loveu.png'
    # not working
    # STREAMING_URL = 'http://www.livestream.com/canalutv'
    LIVESTREAMER_URL = 'http://original.livestream.com/canalutv'
