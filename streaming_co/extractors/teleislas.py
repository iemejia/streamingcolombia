#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class TeleIslasExtractor(StaticExtractor):

    NAME = u'Tele Islas'
    WEBPAGE_URL = 'http://www.teleislas.com.co/'
    LOGO_URL = 'http://www.teleislas.com.co/site/templates/teleisla2013/images/page/Logo.png'
    STREAMING_URL = 'http://xteleislasx.api.channel.livestream.com/3.0/playlist.m3u8'
    LIVESTREAMER_URL = 'http://new.livestream.com/accounts/6205660/events/2583468'
    IS_PLAYABLE = False
