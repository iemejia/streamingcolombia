#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from extractors import *

extractors = [CanalCapitalExtractor(), CanalColombiaExtractor(),
              SenalInstitucionalExtractor(),
              SenalColombiaExtractor(), Canal13Extractor(),
              TeleCaribeExtractor(), TelePacificoExtractor(),
              CanalTROExtractor(), TeleMedellinExtractor()]


ITEM = '#EXTINF:0, '


def generate_m3u_file():
    s = u'#EXTM3U' + '\n'
    for e in extractors:
        s += ITEM + e.NAME + '\n'
        s += e.get_streaming_url() + '\n'
    return s


def get_channels():
    """ Returns a dictionnary of channel information """
    """ This is a convenience method for compatibility with the xbmc plugin """
    """ see https://github.com/diegofn/wiiego-xbmc-addons.git """
    """ title, image_url, streaming_url """
    channels = []
    for e in extractors:
        channels.append({'title': e.NAME, 'image_url': e.LOGO_URL,
                         'streaming_url': e.get_streaming_url()})
    return channels

if __name__ == "__main__":
    print(generate_m3u_file())
