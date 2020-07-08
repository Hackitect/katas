#!/bin/bash
VIDEOS="videos"
MUSIC="music"
IMAGES="images"

[ ! -d "$VIDEOS" ] && mkdir -p "$VIDEOS"
[ ! -d "$MUSIC" ] && mkdir -p "$MUSIC"
[ ! -d "$IMAGES" ] && mkdir -p "$IMAGES"

[ -f "*.mp3" ]  && mv *.mp3 music/
mv *.flac music/
mv *.jpg images/
mv *.png images/
mv *.avi videos/
mv *.mov videos/
rm -f *.log