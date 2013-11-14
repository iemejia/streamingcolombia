#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor
from utils import *


class CableNoticiasExtractor(StaticExtractor):

    NAME = u'Cable Noticias'
    WEBPAGE_URL = 'http://www.cablenoticias.tv/'
    LOGO_URL = 'http://www.cablenoticias.tv/images/logoCableCabezote.png'
    STREAMING_URL = 'rtmp://50.23.172.98:1935/live/cablenoticiastv'