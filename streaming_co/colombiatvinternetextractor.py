#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree
from xml.dom import minidom

from extractors import *
from version import *

import subprocess
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
        """ This is a convenience method for compatibility with the xbmc """
        """ plugin, see https://github.com/diegofn/wiiego-xbmc-addons.git """
        """ title, image_url, streaming_url """
        channels = []
        for e in self.extractors:
            if e.STREAMING_URL or e.LIVESTREAMER_URL:
                channels.append({'title': e.NAME, 'image_url': e.LOGO_URL,
                                 'streaming_url': e.STREAMING_URL,
                                 'livestreamer_url': e.LIVESTREAMER_URL})
        return channels

    def generate_m3u_file(self):
        extractors = [e for e in self.extractors if e.STREAMING_URL]
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
        extractors = [e for e in self.extractors if e.STREAMING_URL]
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
        extractors = [e for e in self.extractors if e.LIVESTREAMER_URL]
        s = '```' + '\n'
        for e in extractors:
            s += '- ' + e.NAME + '\n'
            s += 'livestreamer ' + e.LIVESTREAMER_URL + ' best' + '\n\n'
        return s + '```'

    def generate_missing_channels(self):
        extractors = [e
                      for e in self.extractors
                      if not e.STREAMING_URL and not e.LIVESTREAMER_URL]
        s = 'missing channels: ' + '\n'
        for e in extractors:
            s += e.NAME + '\n'
        return s

    def player(self, cmd="vlc"):
        extractors = [e
                      for e in self.extractors
                      if e.STREAMING_URL or e.LIVESTREAMER_URL]
        for i, e in enumerate(extractors, 1):
            print("%d %s" % (i, e.NAME))
        sel = int(input('Choose a channel: ')) - 1

        e = extractors[sel]
        if e.STREAMING_URL:
            subprocess.call([cmd, e.STREAMING_URL])
        elif e.LIVESTREAMER_URL:
            if not cmd:
                subprocess.call(['livestreamer', e.LIVESTREAMER_URL, 'best'])
            else:
                p1 = subprocess.Popen(['livestreamer', e.LIVESTREAMER_URL, 'best',
                                       '-O'], stdout=subprocess.PIPE)
                p2 = subprocess.Popen([cmd, '-'], stdin=p1.stdout)
                # p1.stdout.close()
                output = p2.communicate()[0]
        else:
            print('invalid extractor information %s' % e)


def display_help():
    print('[streaming-co] version %s' % VERSION)
    print('posible uses:')
    print('$ python streaming-co m3u')
    print('$ python streaming-co xml')
    print('$ python streaming-co livestreamer')
    print('$ python streaming-co missing')
    print('$ python streaming-co player [vlc (default) | cvlc | mplayer | mpv | ffplay | avplay]')


if __name__ == "__main__":
    args = sys.argv[1:]
    coltv = ColombiaTVInternetExtractor()
    if len(args) >= 1:
        if args[0] == 'm3u':
            print(coltv.generate_m3u_file())
        elif args[0] == 'xml':
            print(coltv.generate_xml_file())
        elif args[0] == 'livestreamer':
            print(coltv.generate_livestreamer_file())
        elif args[0] == 'missing':
            print(coltv.generate_missing_channels())
        elif args[0] == 'player':
            cmd = args[1] if len(args) == 2 else 'vlc'
            coltv.player(cmd)
        elif args[0] == '-v' or args[0] == 'version':
            print('[streaming-co] version %s' % VERSION)
        else:
            print('unknown option [%s]' % args[0])
            display_help()
        exit(0)
    else:
        display_help()
