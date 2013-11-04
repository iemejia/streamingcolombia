#!/usr/local/bin/env python

from .staticextractor import StaticExtractor
from utils import *


class CanalTROExtractor(StaticExtractor):

    NAME = 'Canal TRO'
    WEBPAGE_URL = 'http://www.canaltro.com/Nuestra-region-Nuestra-television/'
    STREAMING_URL = 'rtmp://cdns724ste1010.multistream.net/canaltro2live/live-500'

if __name__ == "__main__":
    e = CanalTROExtractor()
    print(e.extract())