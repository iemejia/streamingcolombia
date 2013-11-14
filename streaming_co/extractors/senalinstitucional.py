#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor
from utils import *


class SenalInstitucionalExtractor(StaticExtractor):

    NAME = u'Señal Institucional'
    WEBPAGE_URL = 'http://www.senalinstitucional.gov.co/'
    STREAMING_URL = 'rtmp://cdns724ste1021.multistream.net/rtvclive/live-500'
