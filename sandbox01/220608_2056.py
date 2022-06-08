from itertools import chain
import math

import wave
import struct
import array

#import numpy as np
from PIL import Image as ImageP

out_put = './out/out.wav'
root_path = '../source/sampleImgMacDura32.png'

im = ImageP.open(root_path)
pixelsize_tuple = im.size
data = im.getdata()

DURATION = 32
sample = 44100
data_range = pixelsize_tuple[0] * pixelsize_tuple[1]
block = math.ceil((sample * DURATION) / data_range)

pixel_chain = chain.from_iterable(data)

pixel = list(pixel_chain)

# xxx: `*2` 範囲外用
channelDataLeft = array.array('f', [0 for num in range(sample * DURATION * 2)])
channelDataRight = array.array('f', [0 for num in range(sample * DURATION * 2)])
#channelDataLeft = [0] * (sample * DURATION)
#channelDataRight = [0] * (sample * DURATION)

print('channelDataLeft len:', len(channelDataLeft))
print('data_range:', data_range)

for i in range(block):
  for k in range(data_range):
    channelDataLeft[i * data_range + k] = (pixel[k * 4 + 0] + 256 * pixel[k * 4 + 1]) / 65535 * 2 - 1
    channelDataRight[i * data_range + k] = (pixel[k * 4 + 2] + 256 * pixel[k * 4 + 3]) / 65535 * 2 - 1

py_buff = []
for left, right in zip(channelDataLeft, channelDataRight):
  py_buff.append(left)
  py_buff.append(right)
  


buf = array.array('f', py_buff)


with wave.open(out_put, mode='wb') as f:
  # # todo: (nchannels, sampwidth, framerate, nframes, comptype, compname)
  param = (2, 4, sample, sample * DURATION, 'NONE', 'not compressed')
  f.setparams(param)
  f.writeframes(buf)

