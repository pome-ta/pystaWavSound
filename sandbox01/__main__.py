import wave
import struct

from PIL import Image as ImageP

out_put = './out/out.wav'
root_path = '../source/sampleImgMacDura32.png'

im = ImageP.open(root_path)
pixelsize_tuple = im.size
data = im.getdata()

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
  wv.append(int(p1 * 32767.0))
  wv.append(int(p2 * 32767.0))
  wv.append(p1)
  wv.append(p2)

# print(wv)

print('wv', len(wv))

sampling_rate = 44100


# max_num = 32767.0 / max(wv)
# wv16 = [int(t * max_num) for t in wv]
# bi_wv = struct.pack('h' * len(wv16), *wv16)
bi_wv = struct.pack('f' * len(wv), *wv)
print(len(bi_wv))
with wave.open(out_put, mode='wb') as f:
  # param = (2, 2, sampling_rate, int(len(bi_wv)/2), 'NONE', 'not compressed')
  param = (2, 2, sampling_rate, len(data), 'NONE', 'not compressed')
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

