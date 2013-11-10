Dev Info
========

Ref. https://es.wikipedia.org/wiki/Anexo:Canales_de_televisi%C3%B3n_de_Colombia

# TODO #

## RCN ##
http://www.canalrcnmsn.com/streamingrcn
IP restricted

curl -v -A "Mozilla/5.0 (iPad; CPU OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25" -X GET http://envivo.canalrcn.com/envivo/canalrcn/playlist.m3u8

vlc -vvv http://envivo.canalrcn.com/envivo/canalrcn/playlist.m3u8 :http-user-agent="Mozilla/5.0 (iPad; CPU OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25"

## Canal Uno ##
http://www.canaluno.com.co/

## Noticias uno ##
http://noticiasunolaredindependiente.com/senal-en-vivo/

## CityTV, no tiene link para senal al vivo ##

## Teleantioquia ##
http://www.teleantioquia.co/en-vivo/
http://www.livestream.com/teleantioquiawebs

## Telecafé ##
http://telecafe.gov.co/en/
http://www.livestream.com/telecafe

## TV Orinoquia ##
http://tvorinoquia.net/
http://tvorinoquia.net/se%C3%B1al-en-vivo.html
usa justin.tv

## NTN24 ##
http://www.ntn24.com/
http://www.ntn24.com/envivo

## Tu Kanal ##
http://www.tukanal.tv/
ustream

## Teleamiga ##
http://www.teleamiga.tv/
mms://208.109.243.17:8081/teleamiga

## Nacion TV ##
http://www.naciontv.co/al_aire.html
ustream

## Eltiempo TV ##
http://www.canaleltiempo.tv/envivo
ooyala.com

## Cable Noticias ##
http://www.cablenoticias.tv/
cablenoticiastv

## Zoom Canal ##
http://www.zoomcanal.com.co/Canalenl%C3%ADnea/tabid/706/Default.aspx
http://www.livestream.com/canalzoomtv

## Señal Senado ##
http://www.senado.gov.co/envivo
mms://190.26.211.99/senado

# DONE #

## Canal Caracol ##
https://www.caracoltv.com/senal-vivo
rtmp://cp101307.live.edgefcs.net/live/V2djhrMTqxeN7cqjwSceDrDk7Im9z-x2_640_360_396@29268

IP restricted
ooyala.com

rtmpdump --rtmp rtmp://cp101307.live.edgefcs.net/live/ \
         --playpath V2djhrMTqxeN7cqjwSceDrDk7Im9z-x2_640_360_396@29268 \
         --swfVfy "http://player.ooyala.com/static/cacheable/d971cae356b4a0f432dd862f67590af6/player_v2.swf?version=2&embedType=nuplayer&embedStyle=mjolnir/[[DYNAMIC]]/3" \
         --app live?_fcs_vhost=cp101307.live.edgefcs.net \
         --flashVer "MAC 11,9,900,117" \
         --pageUrl http://www.caracoltv.com/senal-vivo \
         --tcUrl rtmp://23.15.5.185/live?_fcs_vhost=cp101307.live.edgefcs.net \
         --live | mplayer -cache 512 -

## Canal 13 ##
http://www.canal13.com.co/
rtmp://cdns724ste1010.multistream.net/canaltr3celive/live-300

## Señal Institucional ##
http://www.senalinstitucional.gov.co/
rtmp://cdns724ste1021.multistream.net/rtvclive/live-500

## Señal Colombia ##
http://www.senalcolombia.tv/player/popupsc/
rtmp://cdns724ste1010.multistream.net/rtvc2live/live-500

# Canal Capital #
http://www.canalcapital.gov.co/
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

## Telemedellin ##
http://www.telemedellin.tv/Paginas/senalenvivo.aspx
http://new.livestream.com/accounts/4608897/events/2230380
* ver esquema de canal capital

## Telecaribe ##
http://www.telecaribe.com.co/index.php?option=com_content&view=article&id=136&Itemid=255
rtmp://cdns724ste1021.multistream.net/telecaribelive/liveDVR-400

## Telepacífico ##
http://www.telepacifico.com/senal-en-vivo
rtmp://cdns724ste1010.multistream.net/telepacificolive/live-300

## Canal TRO ##
http://www.canaltro.com/Nuestra-region-Nuestra-television/
rtmp://cdns724ste1010.multistream.net/canaltro2live/live-500

