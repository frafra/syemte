#!/usr/bin/env python3

import sys
sys.path.insert(0, '.')

from syemte import syemte

track = syemte.Track(bpm=180, sample="glass")
track.add_silence(70)
for i in range(2):
    track.add_notes(1, "e6")     # you   / you
    track.add_notes(1, "eb6")    # can   / can
    track.add_notes(1, "e6")     # bla-  / run
    track.add_notes(1, "eb6")    # -...- / a-
    track.add_notes(7, "e6")     # -me   / round
    track.add_notes(2, "e6")     # try   / e-
    track.add_notes(1, "e6")     # to    / -ven
    track.add_notes(1, "e6")     # shame / put
    if i == 0:
        track.add_notes(7, "d6") # me    /
    else:
        track.add_notes(1, "d6") #       / me
        track.add_notes(6, "d6") #       / down
    track.add_notes(1, "db6")    # and   / still 
    track.add_notes(2, "d6")     # I     / I'll
    track.add_notes(1, "e6")     # still / be
    track.add_notes(5, "db6")    # care  / there
    track.add_notes(1, "db6")    # for   / for
    track.add_notes(16, "db6")   # you   / you

track.add_silence(1)
track.add_notes(1, "a5")         # the
track.add_notes(9, "gb6")        # world
track.add_notes(1, "gb6")        # may
track.add_notes(1, "ab6")        # think
track.add_notes(1, "a6")         # I'm
track.add_notes(1, "b6")         # foo-
track.add_notes(5, "a6")         # -lish
track.add_notes(3, "ab6")        # they
track.add_notes(3, "gb6")        # can't
track.add_notes(6, "e6")         # see
track.add_notes(3, "db6")        # like
track.add_notes(2, "gb6")        # I
track.add_notes(1, "e6")         # ...
track.add_notes(1, "gb6")        # can
track.add_notes(8, "e6")         # ...
track.add_notes(2, "b5")         # oh
track.add_notes(1, "b5")         # but
track.add_notes(1, "db6")        # a-
track.add_notes(1, "b5")         # -ny-
track.add_notes(6, "a5")         # -one
track.add_notes(1, "gb5")        # who
track.add_notes(2, "a5")         # knows
track.add_notes(1, "db6")        # what
track.add_notes(1, "e6")         # love
track.add_notes(10, "e6")        # is
track.add_notes(1, "ab6")        # will
track.add_notes(5, "ab6")        # un-
track.add_notes(1, "a6")         # -der-
track.add_notes(6, "a6")         # -stand
track.add_notes(11, "g6")        # ...

track.export("output/track2.wav")

