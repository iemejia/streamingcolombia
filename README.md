Streaming Colombia
==================

This project contains utils to watch streaming media from Colombia.

# Preliminaries

You need to install a video player software that supports (rtmp and
mms streams), we recommend you to use
[VLC](http://www.videolan.org/vlc/) which is supported in most
platforms.

Most of the instructions in this README have been tried only in linux.

# Method 1: Using the streaming playlist

Open VLC and choose the open network option and put the following URL:
https://raw.github.com/iemejia/streamingcolombia/master/tvcolombia-static.m3u

Enjoy !

## Stream Capture

You can also play (and capture) individual streams from the individual rtmp
channels of the playlist using rtmpdump, mplayer or ffplay e.g.

e.g. to play Señal Institucional, look for the URL and then use your
favorite video player: vlc, ffplay, avplay, etc.

	ffplay rtmp://cdns724ste1021.multistream.net/rtvclive/live-500

to capture Señal Institucional:

	rtmpdump -o senalinstitucional.flv -r rtmp://cdns724ste1021.multistream.net/rtvclive/live-500

# Method 2: Reproducing with livestreamer

Many channels have dynamic streams who must be captured using the
[livestreamer](http://livestreamer.tanuki.se/en/latest/) utility. To
do so you have to first install the program with:

    pip install livestreamer

then you can execute the given command:

    livestreamer URL QUALITY

You can find the list of valid commoands to reproduce the channels with
livestreamer [here](tvcolombia-livestreamer.md).

Notice that you can replace the last word for quality with *best* or *worst*
depending on your connection speed.

## Stream capture

You can also watch and capture the video piping the stream to a file
and reproducing it with vlc. Thanks to
[@rgamez](https://github.com/rgamez) for the tip.

	livestreamer http://www.ustream.tv/channel/tukanalchannel best -O | tee out.mp4 | vlc -

when you close vlc the recording stops and you can play your saved
out.mp4 file.


# Frequently Asked Questions (FAQ)

## Is there a windows or more user friendly version ?

No, but if you want to contribute you are welcome. On the other hand
you can see the next question.

## Can I use this script with XBMC ?

There is not a plugin for this project for the moment.

You can add the streaming address to XBMC, using the Live TV functionality or the live streams plugin.

I would love to have this project integrated into a nice XBMC plugin,
but I dont have the time to do so for the moement. Again if you want
to help to do this, please contact me and we can share the work.

Note that rhere is also an XBMC plugin for colombian TV that works
only if you are part of the UNE network, you can find it here:
[TVColombia](https://github.com/diegofn/wiiego-xbmc-addons.git).

## Are you ever going to translate these instructions to spanish ?

I am lazy but if you want to just do a pull request with the
instructions in spanish, I will be glad to add them.

# Development

More details on development info and channel extraction can be found
in the file
[DEVELOPMENT.md](https://github.com/iemejia/streamingcolombia/blob/master/DEVELOPMENT.md).

## Generate playlist

You need to install python 3 on your system, then execute:

	python streaming-co m3u > playlist.m3u

and then open the file (playlist.m3u) with VLC.

# Legal

The channels in this project are available freely in the Internet, we
are not pirating or retransmitting anything, just repackaging official
channels in a more convenient manner (with no flash or need of
browsers).

This project includes exclusively TV Channels from Colombia, and it uses their
'official' source locations for streaming.
