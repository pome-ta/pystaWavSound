from math import pi, sin
import wave
import struct
import array

out_put = './out/sin_wave.wav'
write_sec = 1
frequency = 440
sampling_rate = 44100

wv = [
  sin(2 * pi * frequency * t / sampling_rate)
  for t in range(sampling_rate * write_sec)
]
# バイナリ化の下準備の下準備
max_num = 32767.0 / max(wv)  # xxx: short ?
print(max(wv))
# バイナリ化の下準備
wv16 = [int(x * max_num) for x in wv]
print(len(wv16))
# バイナリ化
bi_wv = struct.pack('h' * len(wv16), *wv16)
print(len(bi_wv))
bibi = struct.pack('f' * len(wv), *wv)
#bibi = b''.join([struct.pack('I', v) for v in wv])
ary = array.array('f', wv)
print(type(ary))

wv32 = [int(sample * 32767.0) for sample in wv]
bibi = struct.pack('h' * len(wv32), *wv32)

#by_wv = bytearray.fromhex(wv16)

with wave.open(out_put, mode='wb') as f:
  # todo: (nchannels, sampwidth, framerate, nframes, comptype, compname)
  param = (1, 2, sampling_rate, len(bi_wv), 'NONE', 'not compressed')  #パラメータ
  f.setparams(param)  #パラメータの設定
  #f.writeframes(bi_wv)  #データの書き込み
  #f.writeframes(ary)  #データの書き込み
  f.writeframes(bibi)  #データの書き込み

  nchannles = f.getnchannels()
  samplewidth = f.getsampwidth()
  framerate = f.getframerate()
  nframes = f.getnframes()
  print(f'Channel num : {nchannles}')
  print(f'Sample width : {samplewidth}')
  print(f'Sampling rate : {framerate}')
  print(f'Frame num : {nframes}')

