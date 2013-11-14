#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor
from utils import *


class TeleCaribeExtractor(StaticExtractor):

    NAME = u'Tele Caribe'
    WEBPAGE_URL = 'http://www.telecaribe.com.co/index.php?option=com_content&view=article&id=136&Itemid=255'
    STREAMING_URL = 'rtmp://cdns724ste1021.multistream.net/telecaribelive/liveDVR-400'
