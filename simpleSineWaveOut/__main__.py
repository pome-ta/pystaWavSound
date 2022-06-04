from math import pi, sin
import wave
import struct


def create_wave(out_path, write_sec, frequency, sampling_rate=44100):
  wv = [
    sin(2 * pi * frequency * t / sampling_rate)
    for t in range(sampling_rate * write_sec)
  ]
  # バイナリ化の下準備の下準備
  max_num = 32767.0 / max(wv)
  # バイナリ化の下準備
  wv16 = [int(x * max_num) for x in wv]
  # バイナリ化
  bi_wv = struct.pack('h' * len(wv16), *wv16)

  with wave.open(out_path, mode='wb') as f:
    # todo: (nchannels, sampwidth, framerate, nframes, comptype, compname)
    param = (1, 2, sampling_rate, len(bi_wv), 'NONE', 'not compressed')  #パラメータ
    f.setparams(param)  #パラメータの設定
    f.writeframes(bi_wv)  #データの書き込み


if __name__ == '__main__':
  out_put = './out/sin_wave.wav'
  sec = 1  #1秒
  f = 440  #ラの音の周波数
  sample_rate = 44100  #サンプリング周波数
  create_wave(out_put, sec, f, sample_rate)

