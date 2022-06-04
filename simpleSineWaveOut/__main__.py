# [pythonで音を鳴らす方法を詳しめに解説 - Qiita](https://qiita.com/ShijiMi-Soup/items/3bbf34911f6e43ee14a3)

import numpy as np
import wave
import struct

write_sec = 1  #1秒
frequency = 440  #ラの音の周波数
sampling_rate = 44100  #サンプリング周波数

t = np.arange(0, sampling_rate * write_sec)  #1秒分の時間の配列を確保
wv = np.sin(2 * np.pi * frequency * t / sampling_rate)

max_num = 32767.0 / max(wv)  #バイナリ化の下準備の下準備

wv16 = [int(x * max_num) for x in wv]  #バイナリ化の下準備
bi_wv = struct.pack('h' * len(wv16), *wv16)  #バイナリ化

with wave.open('./out/sin_wave.wav', mode='wb') as f:
  param = (1, 2, sampling_rate, len(bi_wv), 'NONE', 'not compressed')  #パラメータ
  f.setparams(param)  #パラメータの設定
  f.writeframes(bi_wv)  #データの書き込み

if __name__ == '__main__':
  pass

