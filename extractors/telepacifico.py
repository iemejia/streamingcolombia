#!/usr/local/bin/env python

from .staticextractor import StaticExtractor
from utils import *


class TelePacificoExtractor(StaticExtractor):

    NAME = 'Tele Pacífico'
    WEBPAGE_URL = 'http://www.telepacifico.com/senal-en-vivo'
    STREAMING_URL = 'rtmp://cdns724ste1010.multistream.net/telepacificolive/live-300'

if __name__ == "__main__":
    e = TelePacificoExtractor()
    print(e.extract())
