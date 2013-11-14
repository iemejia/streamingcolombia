#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class NacionTVExtractor(StaticExtractor):

    NAME = u'Nación TV'
    WEBPAGE_URL = 'http://www.naciontv.co/al_aire.html'
    LOGO_URL = 'http://www.naciontv.co/_interfAz_CK!/naciontv.png'
    STREAMING_URL = 'rhttp://sjc-uhls-vip03.ustream.tv/watch/playlist.m3u8?cid=14418655&appType=11&appVersion=2&locks=97d170e1550eee4afc0af065b78cda302a97674c&geo=GB&geocity=Glasgow&userId=882388414&connectionId=sjc-ums10_882388414&ts=1384471278&ip=90.244.223.62&sgn=45549b17cbe08ebeb2df752b27987949a2876ab1'
