#!/usr/bin/env python3

import sys
sys.path.insert(0, '.')

from syemte import syemte

track = syemte.Track(bpm=180, sample="glass")
for t2 in range(3):
    for t1 in range(4):
        for tone in ["a6", "e6", "db6"]: # A
            track.add_notes(1, tone)
    for t1 in range(4):
        for tone in ["g6", "d6", "b5"]: # G
            track.add_notes(1, tone)
for t2 in range(4):
    for t1 in range(4):
        for tone in ["a5", "e5", "db5"]: # A
            track.add_notes(1, tone)
    for t1 in range(4):
        for tone in ["g5", "d5", "b4"]: # G
            track.add_notes(1, tone)

for t1 in range(12):
    track.add_notes(1, "gb5", "a5", "d6") # D
for t1 in range(6):
    track.add_notes(1, "f5", "a5", "d6") # Dm
for t1 in range(6):
    track.add_notes(1, "ab5", "b6", "e6") # E
for t1 in range(12):
    track.add_notes(1, "ab5", "db6", "e6") # Cm
for t1 in range(12):
    track.add_notes(1, "gb5", "bb5", "db6") # F#
for t1 in range(12):
    track.add_notes(1, "gb5", "b5", "eb6") # B
for t1 in range(12):
    track.add_notes(1, "ab5", "b5", "e6") # E
for t1 in range(6):
    track.add_notes(1, "ab5", "b5", "eb6") # G#m
for t1 in range(6):
    track.add_notes(1, "a5", "db5", "e6") # A
for t1 in range(12):
    track.add_notes(1, "g5", "b5", "d6") # G
for t2 in range(2):
    for t1 in range(4):
        for tone in ["a6", "e6", "db6"]:
            track.add_notes(1, tone)
    for t1 in range(4):
        for tone in ["g6", "d6", "b5"]:
            track.add_notes(1, tone)

track.export("output/track1.wav")

