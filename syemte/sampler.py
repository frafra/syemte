#!/usr/bin/env python3

import os
import shutil
import subprocess

SAMPLEDIR = 'samples'

def sampler(filepath, target, name, note):
    progression = ['c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'b']
    tone, octave = note[:-1], int(note[-1])

    for semitone in range(-24, 24):
        output = progression[(progression.index(tone)+semitone)%12]
        output += str(octave+(progression.index(tone)+semitone)//12)
        command = f"rubberband -p {semitone} {filepath} {target}/{output}.wav"
        subprocess.check_output(command, shell=True)

for item in os.listdir(SAMPLEDIR):
    filepath = os.path.join(SAMPLEDIR, item)
    if not os.path.isfile(filepath):
        continue
    name, *note = item.rstrip('.wav').rsplit('-', 1)
    target = os.path.join('output', SAMPLEDIR, name)
    os.makedirs(target, exist_ok=True)
    if note:
        sampler(filepath, target, name, note[0])
    else:
        shutil.copyfile(filepath, os.path.join(target, item))
