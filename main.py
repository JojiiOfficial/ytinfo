#!/usr/bin/env python3
import json
import sys
import youtube_dl

video = youtube_dl.YoutubeDL({'quiet': True}).extract_info(sys.argv[1], download=False)

toRemoveKeys = ['formats','requested_formats','automatic_captions']

for tag in toRemoveKeys:
    if tag in video:
        del video[tag]

print(json.dumps(video, indent=4))
