#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class CanalCNCPastoExtractor(StaticExtractor):

    NAME = u'Canal CNC Pasto'
    WEBPAGE_URL = 'http://www.globaltvpasto.com/canales.php/'
    LOGO_URL = ''
    STREAMING_URL = 'http://m.iblups.com:1935/live/JDBZbzVmj6/playlist.m3u8'
