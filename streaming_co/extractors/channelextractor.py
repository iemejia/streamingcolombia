#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


class ChannelExtractor():

	NAME = ''
	WEBPAGE_URL = ''
	IS_PLAYABLE = True
	LOGO_URL = ''

	def get_streaming_url(self):
		""" each channel extractor must implement extract """
		return ''
