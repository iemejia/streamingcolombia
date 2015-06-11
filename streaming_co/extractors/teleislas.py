# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class TeleIslasExtractor(StaticExtractor):

    NAME = u'Tele Islas'
    WEBPAGE_URL = 'http://www.teleislas.com.co/'
    LOGO_URL = 'http://www.teleislas.com.co/site/templates/teleisla2013/images/page/Logo.png'
    STREAMING_URL = 'http://cdnvideo.webvideocore.net/live3ch/out_4r27ggewzxycowws80ck/index.m3u8'
    # not working
    # LIVESTREAMER_URL = 'http://new.livestream.com/accounts/6205660/events/2583468'
