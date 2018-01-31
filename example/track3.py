#!/usr/bin/env python3

import sys
sys.path.insert(0, '.')

from syemte import syemte

track = syemte.Track(bpm=180, sample="clap")
track.add_silence(24)
for t2 in range(2):
    for t1 in range(4):
        track.add_notes(1/2, "clap") # A-
        track.add_notes(1/2, "clap") # -ny-
        track.add_notes(1/2, "clap") # one!
        track.add_silence(1/2+10)
    track.add_silence(192)

track.export("output/track3.wav")
