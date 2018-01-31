#!/usr/bin/env python3

from pydub import AudioSegment

t1 = AudioSegment.from_file("output/track1.wav", format="wav")-10
t2 = AudioSegment.from_file("output/track2.wav", format="wav")
t3 = AudioSegment.from_file("output/track3.wav", format="wav")-15
t4 = AudioSegment.from_file("output/track4.wav", format="wav")-10
played_togther = t1.overlay(t2).overlay(t3).overlay(t4).fade_out(12000)

file_handle = played_togther.export("output/anyone.wav", format="wav")
