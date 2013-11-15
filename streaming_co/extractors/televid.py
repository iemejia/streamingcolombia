#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .livestreamextractor import LiveStreamExtractor


class TeleVidExtractor(LiveStreamExtractor):

    NAME = u'Tele Vid'
    WEBPAGE_URL = 'http://televid.org/televid/'
    LOGO_URL = 'http://televid.org/televid/templates/televid12/images/object979167786.png'
    account_id = '5864544'
    event_id = '2511887'
    IS_PLAYABLE = False
