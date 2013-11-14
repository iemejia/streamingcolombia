#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .channelextractor import ChannelExtractor


class StaticExtractor(ChannelExtractor):

    STREAMING_URL = ''

    def get_streaming_url(self):
        return self.STREAMING_URL
