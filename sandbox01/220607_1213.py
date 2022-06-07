import wave
import struct
import array
import math


import numpy as np
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

pixel = []
for d in data:
  r, g, b, a = d
  pixel.append(r)
  pixel.append(g)
  pixel.append(b)
  pixel.append(a)




wv = []
for d in data:
  r, g, b, a = d
  #wv.append((r + 256 * g) / 65535)
  #wv.append((b + 256 * a) / 65535)
  # print((b + 256 * a) / 65535 * 2 - 1)
  # print(d)
  # print(r, g, b, a)
  p1 = (r + 256 * g) / 65535 * 2 - 1
  p2 = (b + 256 * a) / 65535 * 2 - 1

  wv.append(p1)
  wv.append(p2)

# print(wv)

print('wv', len(wv))

sampling_rate = 44100

# max_num = 32767.0 / max(wv)
# wv16 = [int(t * max_num) for t in wv]
# bi_wv = struct.pack('h' * len(wv16), *wv16)
bi_wv = struct.pack('f' * len(wv), *wv)
bi_wv = array.array('f', wv)
print(len(bi_wv))
with wave.open(out_put, mode='wb') as f:
  # param = (2, 2, sampling_rate, int(len(bi_wv)/2), 'NONE', 'not compressed')
  param = (2, 4, sampling_rate, len(data), 'NONE', 'not compressed')
  f.setparams(param)
  f.writeframes(bi_wv)
  nchannles = f.getnchannels()
  samplewidth = f.getsampwidth()
  framerate = f.getframerate()
  nframes = f.getnframes()
  print(f'Channel num : {nchannles}')
  print(f'Sample width : {samplewidth}')
  print(f'Sampling rate : {framerate}')
  print(f'Frame num : {nframes}')

