#!/usr/local/bin/env python

from extractors.canalcapital import CanalCapitalExtractor
from extractors.senalinstitucional import SenalInstitucionalExtractor
from extractors.senalcolombia import SenalColombiaExtractor
from extractors.canal13 import Canal13Extractor
from extractors.telecaribe import TeleCaribeExtractor
from extractors.telemedellin import TeleMedellinExtractor

extractors = [CanalCapitalExtractor(), SenalInstitucionalExtractor(),
              SenalColombiaExtractor(), Canal13Extractor(),
              TeleCaribeExtractor(), TeleMedellinExtractor()]


ITEM = '#EXTINF:0, '


def generate_m3u_file():
    s = '#EXTM3U' + '\n'
    for e in extractors:
        s += ITEM + e.NAME + '\n'
        s += e.extract() + '\n'
    return s

if __name__ == "__main__":
    print(generate_m3u_file())
