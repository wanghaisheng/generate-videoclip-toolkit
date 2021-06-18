#!/usr/bin/env python3

from clip3 import *

# solid(640, 480, 30, 300, [0,0,0]).save('black.mp4')
# solid(640, 480, 30, 300, [255,0,0]).save('red.mp4')
# solid(640, 480, 30, 300, [0,255,0]).save('green.mp4')
# solid(640, 480, 30, 300, [0,0,255]).save('blue.mp4')
# solid(640, 480, 30, 300, [255,255,255]).save('white.mp4')


temporal_composite(
  (solid(640, 480, 30, 5, [0,0,0]), 0),
  (solid(640, 480, 30, 5, [255,0,0]), 4.5)
).save('tc.mp4')
