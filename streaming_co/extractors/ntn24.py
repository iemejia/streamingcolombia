#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class NTN24Extractor(StaticExtractor):

    NAME = u'NTN24'
    WEBPAGE_URL = 'http://www.ntn24.com/envivo'
    LOGO_URL = 'http://www.ntn24.com/sites/all/themes/ntn24/images/logontn24.png'
    STREAMING_URL = 'http://www.youtube.com/watch?v=xzMfw-N7LZc#t=79026'
    IS_PLAYABLE = False
