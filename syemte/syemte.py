from pydub import AudioSegment

import functools
import os.path

class Track:
    def __init__(self, bpm=60, path='output/samples', sample=''):
        self.beat = int(60*1000/bpm)
        self.path = path
        self.sample = sample
        self.track = AudioSegment.empty()
        self.cursor = 1
    def export(self, filename):
        self.track.export(filename, format="wav")
    def add_silence(self, duration=1):
        silence = AudioSegment.silent(self.beat*duration)
        self.track += silence
        self.cursor += self.beat*duration
    def get_wav(self, tone):
        filepath = os.path.join(self.path, self.sample, tone+'.wav')
        return AudioSegment.from_file(filepath, format="wav")
    def add_notes(self, duration, *tones):
        silence = AudioSegment.silent(duration=self.cursor)
        segments = [self.get_wav(tone) for tone in tones]
        tone = functools.reduce(lambda s1, s2: s1.overlay(s2), segments)
        self.track = (silence+tone).overlay(self.track)
        self.cursor += self.beat*duration

