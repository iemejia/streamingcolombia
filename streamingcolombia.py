#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from extractors import *

extractors = [CanalCapitalExtractor(), SenalInstitucionalExtractor(),
              SenalColombiaExtractor(), Canal13Extractor(),
              TeleCaribeExtractor(), TelePacificoExtractor(),
              CanalTROExtractor(), TeleMedellinExtractor()]


ITEM = '#EXTINF:0, '


def generate_m3u_file():
    s = '#EXTM3U' + '\n'
    for e in extractors:
        s += ITEM + e.NAME + '\n'
        s += e.extract() + '\n'
    return s

if __name__ == "__main__":
    print(generate_m3u_file())
