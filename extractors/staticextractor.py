#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from .extractor import Extractor

class StaticExtractor(Extractor):

	STREAMING_URL = ''

	def extract(self):
		return self.STREAMING_URL
