#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class CMBTelevisionExtractor(StaticExtractor):

    NAME = u'CMB Televisión'
    WEBPAGE_URL = 'http://www.cmbcolombia.tv/'
    LOGO_URL = 'http://www.cmbcolombia.tv/images/logo_cmb.png'
    STREAMING_URL = 'rtmp://hd.worldkast.com:1935/8076/_definst_/mp4:80763'
