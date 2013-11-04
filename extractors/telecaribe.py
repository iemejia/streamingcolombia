#!/usr/local/bin/env python

from .staticextractor import StaticExtractor
from utils import *


class TeleCaribeExtractor(StaticExtractor):

    NAME = 'Tele Caribe'
    WEBPAGE_URL = 'http://www.telecaribe.com.co/index.php?option=com_content&view=article&id=136&Itemid=255'
    STREAMING_URL = 'rtmp://cdns724ste1021.multistream.net/telecaribelive/liveDVR-400'

if __name__ == "__main__":
    e = TeleCaribeExtractor()
    print(e.extract())
