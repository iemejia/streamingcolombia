#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


class ChannelExtractor():

	NAME = None
	WEBPAGE_URL = None
	IS_PLAYABLE = True
	LOGO_URL = None
	LIVESTREAMER_URL = None

	def get_streaming_url(self):
		""" each channel extractor must implement extract """
		return ''
