from pathlib import Path
import array
import wave

wav_data_path = Path('./dump/wavData.txt')
#wav_txt = wav_data_path.read_text()

DURATION = 0.1
sample = 44100

with open(wav_data_path, encoding='utf_8') as f:
  l_strip = [float(s.strip()) for s in f.readlines()]
  #print(l_strip)

buf = array.array('f', l_strip)
out_put = './out/out.wav'

with wave.open(out_put, mode='wb') as f:
  # # todo: (nchannels, sampwidth, framerate, nframes, comptype, compname)
  param = (2, 4, sample, int(sample * DURATION), 'NONE', 'not compressed')
  f.setparams(param)
  f.writeframes(buf)


