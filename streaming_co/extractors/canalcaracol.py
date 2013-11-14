#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor
from utils import *


class CanalColombiaExtractor(StaticExtractor):

    NAME = u'Canal Caracol'
    WEBPAGE_URL = 'https://www.caracoltv.com/senal-vivo'
    LOGO_URL = 'http://st.caracoltv.co/sites/caracoltv.com/themes/caracol/images/programasProd/logo_big.png'
    STREAMING_URL = 'rtmp://cp101307.live.edgefcs.net/live/V2djhrMTqxeN7cqjwSceDrDk7Im9z-x2_640_360_396@29268'
    IS_PLAYABLE = False