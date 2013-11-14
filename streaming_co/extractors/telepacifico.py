#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor
from utils import *


class TelePacificoExtractor(StaticExtractor):

    NAME = u'Tele Pacífico'
    WEBPAGE_URL = 'http://www.telepacifico.com/senal-en-vivo'
    LOGO_URL = 'http://www.telepacifico.com/themes/telepacificotheme/images/logo.png'
    STREAMING_URL = 'rtmp://cdns724ste1010.multistream.net/telepacificolive/live-300'
