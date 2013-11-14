Streaming Colombia
==================

This project contains utils to watch streaming media from Colombia.
Basically it consists of an script (streaming-co) that generates a
playlist (m3u file) of live TV streaming channels from Colombia.

# Instructions 

You need to install a video player software that supports (rtmp and
mms streams), we recommend you to use
[VLC](http://www.videolan.org/vlc/) which is supported in most
platforms.

## static version

This version is more limited and includes less channel but has the convinience
that you you don't need any additional software in your system.

Open VLC and choose the open network option and put the following URL:
https://raw.github.com/iemejia/streamingcolombia/master/tvcolombia-static.m3u

Enjoy!

## dynamic version (supports more channels)

You need to install python 2.6 or superior on your system, then execute:

	python streaming-co > playlist.m3u
	
and then open the file (playlist.m3u) with VLC. 

## XBMC

We are working towards the integration of this project into the
TVColombia XBMC plugin, for more info see
[TVColombia](https://github.com/diegofn/wiiego-xbmc-addons.git).

## advanced users

You can also play (and capture) individual streams from the individual rtmp 
channels of the playlist using rtmpdump, mplayer or ffplay e.g.

to play Señal Institucional, look for the URL and then:

	ffplay rtmp://cdns724ste1021.multistream.net/rtvclive/live-500

to capture Señal Institucional:

	rtmpdump -o senalinstitucional.flv -r rtmp://cdns724ste1021.multistream.net/rtvclive/live-500

# Legal

The channels in this project are available freely in the Internet, we are not
pirating or retransmitting anything, just repackaging official channels 
in a more convenient manner.

This project includes exclusively TV Channels from Colombia, and it uses their 
'official' source locations for streaming.

# Development

More details on development info and channel extraction can be found
in the file
[dev.md](https://github.com/iemejia/streamingcolombia/blob/master/dev.md).
