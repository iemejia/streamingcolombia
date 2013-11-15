#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class CanalDCExtractor(StaticExtractor):

    NAME = u'Canal DC'
    WEBPAGE_URL = 'http://www.canaldc.tv/sitio/'
    LOGO_URL = 'http://www.canaldc.tv/sitio/templates/dinamikos_canaldc/images/red/logo.png'
    STREAMING_URL = 'rtmp://cdns724ste0010.multistream.net/stream1215live/live-250'
