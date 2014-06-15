#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class CanalCaracolExtractor(StaticExtractor):

    NAME = u'Canal Caracol'
    WEBPAGE_URL = 'https://www.caracoltv.com/senal-vivo'
    LOGO_URL = 'http://st.caracoltv.co/sites/caracoltv.com/themes/caracol/images/programasProd/logo_big.png'
    STREAMING_URL = 'rtmp://cp101307.live.edgefcs.net/live/V2djhrMTqxeN7cqjwSceDrDk7Im9z-x2_640_360_396@29268'
    LIVESTREAMER_URL = 'hds://http://acaooyalahd2-lh.akamaihd.net/z/caracol01_delivery@187698/manifest.f4m?hdcore=2.10.3&g=PEWEWKTRRUJM'
    IS_PLAYABLE = False
