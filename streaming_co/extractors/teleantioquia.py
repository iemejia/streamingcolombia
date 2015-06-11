# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class TeleAntioquiaExtractor(StaticExtractor):

    NAME = u'Teleantioquia'
    WEBPAGE_URL = 'http://www.teleantioquia.co/en-vivo/'
    LOGO_URL = 'http://www.teleantioquia.co/v2_base/file_loader.php?id_file=12080-m21'
    # STREAMING_URL = 'http://xteleantioquiawebsx.api.channel.livestream.com/3.0/playlist.m3u8'
    LIVESTREAMER_URL = 'http://livestream.com/accounts/9427524/events/3496592/'
