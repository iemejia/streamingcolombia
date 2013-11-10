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
        s += e.extract() + '\n'
    return s

if __name__ == "__main__":
    print(generate_m3u_file())
