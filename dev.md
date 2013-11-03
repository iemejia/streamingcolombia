Dev Info
========

# Canal Capital #

http://new.livestream.com/accounts/4239881/events/2169976

livestream.com

http://new.livestream.com/api/accounts/[account_id]/events/[event_id]/viewing_info
http://new.livestream.com/api/accounts/4239881/events/2169976/viewing_info

{"real_time":{"path":"/events/2169976","namespace":"/events","roomId":2169976},"streamInfo":{"event_id":2169976,"broadcast_id":33720469,"broadcast_created_at":"2013-11-01T19:55:11.159Z","is_live":true,"stream_title":"Canal Capital","qualities":[{"name":"Normal Quality","bitrate":446000,"width":512,"height":384}],"thumbnail_url":"http://img.new.livestream.com/events/0000000000211c78/33f08fca-d009-4768-8fcd-305d8a435e94_15420.jpg","live_video_post_id":33720468,"play_url":"http://api.new.livestream.com/broadcasts/33720469.smil","m3u8_url":"http://api.new.livestream.com/broadcasts/33720469.m3u8?dw=100","rtsp_url":"rtsp://212-125.livestream.com:8080/livestreamiphone/4239881_2169976_4e9fca3d_1_446@117636"},"generated_at":"2013-11-02T00:13:00.860Z"}

then request play_url
http://api.new.livestream.com/broadcasts/33720469.smil

<smil xmlns="http://www.w3.org/2001/SMIL20/Language">
<head>
<meta name="title" content="4239881_2169976_4e9fca3d_1"/>
<meta name="httpBase" content="http://livestream-f.akamaihd.net/"/>
</head>
<body>
<switch id="4239881_2169976_4e9fca3d_1">
<video src="4239881_2169976_4e9fca3d_1_446@117636" system-bitrate="446000"/>
</switch>
</body>
</smil>

and with this build the real address that it is:
head.httpBase content + video.src
http://livestream-f.akamaihd.net/4239881_2169976_4e9fca3d_1_446@117636

# RCN #
http://www.canalrcnmsn.com/streamingrcn
IP restricted

# Caracol #
https://www.caracoltv.com/senal-vivo
IP restricted

rtmpdump --rtmp rtmp://cp101307.live.edgefcs.net/live/ \
         --playpath V2djhrMTqxeN7cqjwSceDrDk7Im9z-x2_640_360_396@29268 \
         --swfVfy "http://player.ooyala.com/static/cacheable/d971cae356b4a0f432dd862f67590af6/player_v2.swf?version=2&embedType=nuplayer&embedStyle=mjolnir/[[DYNAMIC]]/3" \
         --app live?_fcs_vhost=cp101307.live.edgefcs.net \
         --flashVer "MAC 11,9,900,117" \
         --pageUrl http://www.caracoltv.com/senal-vivo \
         --tcUrl rtmp://23.15.5.185/live?_fcs_vhost=cp101307.live.edgefcs.net \
         --live | mplayer -cache 512 -

# Canal Uno #
http://www.canaluno.com.co/

## Noticias uno
http://noticiasunolaredindependiente.com/senal-en-vivo/

# CityTV, no tiene link para senal al vivo

# Eltiempo TV #
http://www.canaleltiempo.tv/envivo

# Teleantioquia #
http://www.teleantioquia.co/en-vivo/

