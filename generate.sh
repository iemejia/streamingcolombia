#!/bin/sh
python3 streaming-co livestreamer > tvcolombia-livestreamer.md
python3 streaming-co m3u > tvcolombia-static.m3u
python3 streaming-co xml > tvcolombia-static.xml
