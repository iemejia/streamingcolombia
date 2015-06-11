# -*- coding: utf-8 -*-

from .staticextractor import StaticExtractor


class SenalInstitucionalExtractor(StaticExtractor):

    NAME = u'Señal Institucional'
    WEBPAGE_URL = 'http://www.senalinstitucional.gov.co/'
    LOGO_URL = 'http://www.senalinstitucional.gov.co/templates/institucional_2013/images/new/logo_institucional_escudo.png'
    # not working
    # STREAMING_URL = 'rtmp://cdns724ste1021.multistream.net/rtvclive/live-500'
    LIVESTREAMER_URL = 'hds://http://cdns840stu1010.multistream.net/rtvclive/amlst:live/manifest.f4m'
