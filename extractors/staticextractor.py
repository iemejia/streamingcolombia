#!/usr/local/bin/env python

from .extractor import Extractor

class StaticExtractor(Extractor):

	STREAMING_URL = ''

	def extract(self):
		return self.STREAMING_URL
