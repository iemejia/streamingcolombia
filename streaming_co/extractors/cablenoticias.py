# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class CableNoticiasExtractor(StaticExtractor):

    NAME = u'Cable Noticias'
    WEBPAGE_URL = 'http://www.cablenoticias.tv/'
    LOGO_URL = 'http://www.cablenoticias.tv/images/logoCableCabezote.png'
    STREAMING_URL = 'rtmp://50.23.173.13:1935/live/cablenoticiastv_720p'
