#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor
from utils import *


class SenalColombiaExtractor(StaticExtractor):

    NAME = u'Señal Colombia'
    WEBPAGE_URL = 'http://www.senalcolombia.tv/player/popupsc/'
    STREAMING_URL = 'rtmp://cdns724ste1010.multistream.net/rtvc2live/live-500'
