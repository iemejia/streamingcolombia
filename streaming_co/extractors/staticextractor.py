# -*- coding: utf-8 -*-

from .channelextractor import ChannelExtractor


class StaticExtractor(ChannelExtractor):

    def get_streaming_url(self):
        return self.STREAMING_URL
