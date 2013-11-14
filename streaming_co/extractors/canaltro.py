#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor
from utils import *


class CanalTROExtractor(StaticExtractor):

    NAME = u'Canal TRO'
    WEBPAGE_URL = 'http://www.canaltro.com/Nuestra-region-Nuestra-television/'
    STREAMING_URL = 'rtmp://cdns724ste1010.multistream.net/canaltro2live/live-500'