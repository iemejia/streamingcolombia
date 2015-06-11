# -*- coding: utf-8 -*-


class ChannelExtractor():

    NAME = None
    WEBPAGE_URL = None
    LOGO_URL = None
    STREAMING_URL = None
    LIVESTREAMER_URL = None

    def get_streaming_url(self):
        """ each channel extractor must implement extract """
        return ''
