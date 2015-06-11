#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree
from xml.dom import minidom

from extractors import *
from version import *

import sys


class ColombiaTVInternetExtractor():

    extractors = [CanalCapitalExtractor(), CanalCaracolExtractor(),
                  CanalRCNExtractor(),
                  SenalInstitucionalExtractor(), SenalColombiaExtractor(),
                  Canal13Extractor(), CableNoticiasExtractor(),
                  CanalDCExtractor(), CanalUExtractor(),
                  ZoomCanalExtractor(), TeleAntioquiaExtractor(),
                  TeleCafeExtractor(), TeleCaribeExtractor(),
                  TelePacificoExtractor(), CanalTROExtractor(),
                  TeleMedellinExtractor(), TVCincoMonteriaExtractor(),
                  TeleIslasExtractor(), NacionTVExtractor(),
                  TuKanalExtractor(),
                  TeleSantanderExtractor(), NTN24Extractor(),
                  TeleVidExtractor(), BugaVisionExtractor(),
                  CanalCNCCaliExtractor(), CanalCNCPastoExtractor(),
                  TeleAmigaExtractor(), CMBTelevisionExtractor()]

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

    def generate_m3u_file(self):
        extractors = [e for e in self.extractors if e.IS_PLAYABLE and e.STREAMING_URL]
        s = u'#EXTM3U' + '\n'
        for e in extractors:
            s += '#EXTINF:0, ' + e.NAME + '\n'
            s += e.get_streaming_url() + '\n'
        return s

    def __prettify__(self, elem):
        # """Return a pretty-printed XML string for the Element. """
        rough_string = ElementTree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

    def generate_xml_file(self):
        extractors = [e for e in self.extractors if e.IS_PLAYABLE and e.STREAMING_URL]
        channels = Element('channels')
        channel = SubElement(channels, 'channel')
        name = SubElement(channel, 'name')
        name.text = 'Streaming Colombia'
        thumbnail = SubElement(channel, 'thumbnail')
        thumbnail.text = 'https://upload.wikimedia.org/wikipedia/commons/f/f8/Flag_of_Colombia.png'

        items = SubElement(channel, 'items')
        for e in extractors:
            item = SubElement(items, 'item')
            title = SubElement(item, 'title')
            title.text = e.NAME
            link = SubElement(item, 'link')
            link.text = e.get_streaming_url()
            item_thumbnail = SubElement(item, 'thumbnail')
            item_thumbnail.text = e.LOGO_URL

        return self.__prettify__(channels)

    def generate_livestreamer_file(self):
        extractors = [e for e in self.extractors if e.IS_PLAYABLE and e.LIVESTREAMER_URL]
        s = ''
        for e in extractors:
            s += '- ' + e.NAME + '\n'
            s += 'livestreamer ' + e.LIVESTREAMER_URL + ' best' + '\n\n'
        return s

    def generate_missing_channels(self):
        extractors = [e for e in self.extractors if not e.IS_PLAYABLE]
        s = 'missing channels: ' + '\n'
        for e in extractors:
           s += e.NAME + '\n'
        return s


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 1:
        if args[0] == 'm3u':
            print(ColombiaTVInternetExtractor().generate_m3u_file())
        if args[0] == 'xml':
            print(ColombiaTVInternetExtractor().generate_xml_file())
        if args[0] == 'livestreamer':
            print(ColombiaTVInternetExtractor().generate_livestreamer_file())
        if args[0] == 'missing':
            print(ColombiaTVInternetExtractor().generate_missing_channels())
        if args[0] == '-v' or args[0] == 'version':
            print('[streaming-co] version %s' % VERSION)
    else:
        print('[streaming-co] version %s' % VERSION)
        print('posible uses:')
        print('$ python streaming-co m3u')
        print('$ python streaming-co xml')
        print('$ python streaming-co livestreamer')
        print('$ python streaming-co missing')
