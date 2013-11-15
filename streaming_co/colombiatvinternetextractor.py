#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from extractors import *
from version import *

import sys


class ColombiaTVInternetExtractor():

    extractors = [CanalCapitalExtractor(), CanalCaracolExtractor(),
                  SenalInstitucionalExtractor(), SenalColombiaExtractor(),
                  Canal13Extractor(), CableNoticiasExtractor(),
                  CanalDCExtractor(),
                  ZoomCanalExtractor(), TeleAntioquiaExtractor(),
                  TeleCafeExtractor(), TeleCaribeExtractor(),
                  TelePacificoExtractor(), CanalTROExtractor(),
                  TeleMedellinExtractor(), TVCincoMonteriaExtractor(),
                  TeleIslasExtractor(), NacionTVExtractor(),
                  TeleSantanderExtractor(), NTN24Extractor(),
                  TeleVidExtractor(), BugaVisionExtractor(),
                  CanalCNCPastoExtractor(),
                  TeleAmigaExtractor(), CMBTelevisionExtractor()]

    def __generate_m3u_file__(self, extractors):
        s = u'#EXTM3U' + '\n'
        for e in extractors:
            s += '#EXTINF:0, ' + e.NAME + '\n'
            s += e.get_streaming_url() + '\n'
        return s

    def generate_all(self):
        extractors = [e for e in self.extractors if e.IS_PLAYABLE]
        return self.__generate_m3u_file__(extractors)

    def get_channels(self):
        """ Returns a dictionnary of channel information """
        """ This is a convenience method for compatibility with the xbmc plugin """
        """ see https://github.com/diegofn/wiiego-xbmc-addons.git """
        """ title, image_url, streaming_url """
        channels = []
        for e in self.extractors:
            if e.IS_PLAYABLE:
                channels.append({'title': e.NAME, 'image_url': e.LOGO_URL,
                                 'is_playable': e.IS_PLAYABLE,
                                 'streaming_url': e.get_streaming_url()})
        return channels

    def generate_static_m3u_file(self):
        extractors = [e for e in self.extractors if issubclass(type(e), StaticExtractor) and e.IS_PLAYABLE]
        return self.__generate_m3u_file__(extractors)

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        print(ColombiaTVInternetExtractor().generate_all())
    elif len(args) == 1:
        if args[0] == 'static':
            print(ColombiaTVInternetExtractor().generate_static_m3u_file())
        if args[0] == 'xbmc':
            print(ColombiaTVInternetExtractor().get_channels())
        if args[0] == '-v' or args[0] == 'version':
            print('[streaming-co] version %s' % VERSION)
    else:
        print('[streaming-co] version %s' % VERSION)
        print('posible uses:')
        print('$ python streaming-co')
        print('$ python streaming-co static')
        print('$ python streaming-co xbmc')
