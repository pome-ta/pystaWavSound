from pathlib import Path
import wave

import struct
#import array
import random

wav_data_path = Path('./dump/wavData.txt')
out_put = './out/reverse.wav'
#wav_txt = wav_data_path.read_text()

DURATION = 16
sample = 44100

with open(wav_data_path, encoding='utf_8') as f:
  l_strip = [float(s.strip()) for s in f.readlines()]

#random.shuffle(l_strip)
l_strip.reverse()
max_num = 32767.0 / max(l_strip)
wv16 = [int(i * max_num) for i in l_strip]
buf = struct.pack('h' * len(wv16), *wv16)
#buf = array.array('f', l_strip)

with wave.open(out_put, mode='wb') as f:
  # # todo: (nchannels, sampwidth, framerate, nframes, comptype, compname)
  param = (2, 2, sample, sample * DURATION, 'NONE', 'not compressed')
  f.setparams(param)
  f.writeframes(buf)

