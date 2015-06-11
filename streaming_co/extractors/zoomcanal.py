# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class ZoomCanalExtractor(StaticExtractor):

    NAME = u'Zoom Canal'
    WEBPAGE_URL = 'http://www.zoomcanal.com.co/Canalenl%C3%ADnea/tabid/706/Default.aspx'
    LOGO_URL = 'http://www.zoomcanal.com.co/Portals/0/img_LogoZoom.jpg'
    STREAMING_URL = 'http://xcanalzoomtvx.api.channel.livestream.com/3.0/playlist.m3u8'
    # LIVESTREAMER_URL = 'http://www.livestream.com/canalzoomtv'
