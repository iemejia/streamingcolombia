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

to play Señal Institucional, look for the URL and then use your
favorite video player, eg.g ffplay, avplay, etc.

	ffplay rtmp://cdns724ste1021.multistream.net/rtvclive/live-500

to capture Señal Institucional:

	rtmpdump -o senalinstitucional.flv -r rtmp://cdns724ste1021.multistream.net/rtvclive/live-500

# Frequently Asked Questions (FAQ)

## Which channels used to work and are disabled in this moment ?

- Canal Capital
- Canal DC
- Canal CNC Cali
- Canal CNC Pasto
- TeleMedellin
- Buga Vision
- TV Cinco Monteria
- Canal TRO
- Tele Santander
- Tele Islas
- NTN24
- Tele Amiga

## Where is Canal Caracol ?

Canal Caracol seems to have changed its video provider and we don't
have yet a solution to include it in the streaming playlist. For the
moment you can play Canal Caracol like this:

	pip install livestreamer

	livestreamer "hds://http://acaooyalahd2-lh.akamaihd.net/z/caracol01_delivery@187698/manifest.f4m?hdcore=2.10.3&g=PEWEWKTRRUJM" best

You can also change the best word in the end for worst if your
connection is not fast enough.

## Where is Canal RCN ?

Canal RCN is not supported for the moment.

## Are you ever going to translate these instructions to spanish ?

I am lazy but if you want to just do a pull request with the
instructions in spanish, I will be glad to add them.

# Legal

The channels in this project are available freely in the Internet, we are not
pirating or retransmitting anything, just repackaging official channels 
in a more convenient manner.

This project includes exclusively TV Channels from Colombia, and it uses their 
'official' source locations for streaming.

# Development

More details on development info and channel extraction can be found
in the file
[DEVELOPMENT.md](https://github.com/iemejia/streamingcolombia/blob/master/DEVELOPMENT.md).
