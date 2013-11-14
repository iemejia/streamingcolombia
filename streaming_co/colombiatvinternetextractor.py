#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from extractors import *


class ColombiaTVInternetExtractor():

    extractors = [CanalCapitalExtractor(), CanalColombiaExtractor(),
                  SenalInstitucionalExtractor(), SenalColombiaExtractor(),
                  Canal13Extractor(), CableNoticiasExtractor(),
                  TeleCaribeExtractor(), TelePacificoExtractor(),
                  CanalTROExtractor(), TeleMedellinExtractor(),
                  TeleAmigaExtractor()]

    def generate_m3u_file(self):
        s = u'#EXTM3U' + '\n'
        for e in self.extractors:
            s += '#EXTINF:0, ' + e.NAME + '\n'
            s += e.get_streaming_url() + '\n'
        return s

    def get_channels(self):
        """ Returns a dictionnary of channel information """
        """ This is a convenience method for compatibility with the xbmc plugin """
        """ see https://github.com/diegofn/wiiego-xbmc-addons.git """
        """ title, image_url, streaming_url """
        channels = []
        for e in self.extractors:
            channels.append({'title': e.NAME, 'image_url': e.LOGO_URL,
                             'is_playable': e.IS_PLAYABLE,
                             'streaming_url': e.get_streaming_url()})
        return channels

if __name__ == "__main__":
    print(ColombiaTVInternetExtractor().generate_m3u_file())
    # print(ColombiaTVInternetExtractor().get_channels())
