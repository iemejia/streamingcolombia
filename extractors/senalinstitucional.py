#!/usr/local/bin/env python

from .staticextractor import StaticExtractor
from utils import *


class SenalInstitucionalExtractor(StaticExtractor):

    NAME = 'Señal Institucional'
    WEBPAGE_URL = 'http://www.senalinstitucional.gov.co/'
    STREAMING_URL = 'rtmp://cdns724ste1021.multistream.net/rtvclive/live-500'

if __name__ == "__main__":
    e = SenalInstitucionalExtractor()
    print(e.extract())
