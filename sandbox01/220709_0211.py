# 複数吐き出し

from pathlib import Path
import wave

import struct
#import array

DURATION = 4
sample = 44100


def create_tones(tone_list):
  for tone in tone_list:
    wav_data_path = Path(f'./dump/{tone}.txt')
    out_put = f'./out/toneOneshot/{tone}.wav'
    l_strip = None
    with open(wav_data_path, encoding='utf_8') as f:
      l_strip = [float(s.strip()) for s in f.readlines()]

    max_num = 32767.0 / max(l_strip)
    # xxx: 音量ミスったから、*0.8 で下げてる
    wv16 = [int(i * max_num * 0.8) for i in l_strip]
    buf = struct.pack('h' * len(wv16), *wv16)

    with wave.open(out_put, mode='wb') as f:
      # # todo: (nchannels, sampwidth, framerate, nframes, comptype, compname)
      param = (2, 2, sample, sample * DURATION, 'NONE', 'not compressed')
      f.setparams(param)
      f.writeframes(buf)


if __name__ == '__main__':
  tones = ['c4', 'd4', 'e4', 'f4', 'g4', 'a4', 'b4', 'c5']
  create_tones(tones)

