# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class TeleCaribeExtractor(StaticExtractor):

    NAME = u'Tele Caribe'
    WEBPAGE_URL = 'http://www.telecaribe.com.co/index.php?option=com_content&view=article&id=136&Itemid=255'
    LOGO_URL = 'http://www.telecaribe.com.co/templates/youshows/images/turquoise/logo.png'
    STREAMING_URL = 'rtmp://cdns724ste1021.multistream.net/telecaribelive/live-400'
    IS_PLAYABLE = False
