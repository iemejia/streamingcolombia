Streaming Colombia
==================

This project contains utils to watch streaming media from Colombia.

# streamingcolombia.py #

This script generates a playlist (m3u file) of live TV streaming channels from Colombia.

To use it, you just have to first generate the playlist file:

	python streamingcolombia.py > playlist.m3u

and then open it with [VLC](http://www.videolan.org/vlc/).

You can also play individual streams with ffplay, e.g.

	ffplay rtmp://cdns724ste1021.multistream.net/rtvclive/live-500

This plugin is compatible with python > 2.6. It doesn't use any additional packages.
