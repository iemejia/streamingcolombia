#!/usr/local/bin/env python

from .staticextractor import StaticExtractor
from utils import *


class SenalColombiaExtractor(StaticExtractor):

    NAME = 'Señal Colombia'
    WEBPAGE_URL = 'http://www.senalcolombia.tv/player/popupsc/'
    STREAMING_URL = 'rtmp://cdns724ste1010.multistream.net/rtvc2live/live-500'

if __name__ == "__main__":
    e = SenalColombiaExtractor()
    print(e.extract())
