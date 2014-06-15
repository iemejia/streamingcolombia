#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class CanalRCNExtractor(StaticExtractor):

    NAME = u'Canal RCN'
    WEBPAGE_URL = 'http://www.canalrcnmsn.com/streamingrcn'
    LOGO_URL = 'http://www.canalrcn.com/sites/default/files/logo-rcn_0.png'
    STREAMING_URL = 'http://ooyalahd2-f.akamaihd.net/z/saleslatam_test06@180219/manifest.f4m?hdcore=2.10.3&g=PEKPFNBGBTUV'
    LIVESTREAMER_URL = 'hds://http://ooyalahd2-f.akamaihd.net/z/saleslatam_test06@180219/manifest.f4m?hdcore=2.10.3&g=PEKPFNBGBTUV'
    IS_PLAYABLE = False
