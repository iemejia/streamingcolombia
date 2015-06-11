# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class Canal13Extractor(StaticExtractor):

    NAME = u'Canal 13'
    WEBPAGE_URL = 'http://www.canal13.com.co/'
    LOGO_URL = 'http://www.canal13.com.co/log_bop.png'
    # not working
    #STREAMING_URL = 'rtmp://cdns724ste1010.multistream.net/canaltr3celive/live-300'
    LIVESTREAMER_URL = 'hds://http://cdns840stu1010.multistream.net/canaltr3celive/amlst:live/manifest.f4m'
