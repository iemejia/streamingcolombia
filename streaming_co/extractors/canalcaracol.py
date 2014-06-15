#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class CanalCaracolExtractor(StaticExtractor):

    NAME = u'Canal Caracol'
    WEBPAGE_URL = 'https://www.caracoltv.com/senal-vivo'
    LOGO_URL = 'http://st.caracoltv.co/sites/caracoltv.com/themes/caracol/images/programasProd/logo_big.png'
    STREAMING_URL = "http://acaooyalahd2-lh.akamaihd.net/i/caracol04_delivery@187706/index_2128_av-b.m3u8?sd=10&rebase=on"
    # LIVESTREAMER_URL = 'hds://http://acaooyalahd2-lh.akamaihd.net/z/caracol01_delivery@187698/manifest.f4m?hdcore=2.10.3&g=PEWEWKTRRUJM'
    IS_PLAYABLE = True
