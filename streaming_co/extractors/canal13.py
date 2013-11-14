#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor
from utils import *


class Canal13Extractor(StaticExtractor):

    NAME = u'Canal 13'
    WEBPAGE_URL = 'http://www.canal13.com.co/'
    STREAMING_URL = 'rtmp://cdns724ste1010.multistream.net/canaltr3celive/live-300'