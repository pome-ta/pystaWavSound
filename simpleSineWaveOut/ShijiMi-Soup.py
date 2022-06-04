import numpy as np
import wave
import struct

sec = 1  #1秒
note_hz = 440  #ラの音の周波数
sample_hz = 44100  #サンプリング周波数
t = np.arange(0, sample_hz * sec)  #1秒分の時間の配列を確保
wv = np.sin(2 * np.pi * note_hz * t / sample_hz)

max_num = 32767.0 / max(wv)  #バイナリ化の下準備の下準備
wv16 = [int(x * max_num) for x in wv]  #バイナリ化の下準備
bi_wv = struct.pack('h' * len(wv16), *wv16)  #バイナリ化

file = wave.open(
  './out/sin_wave.wav',
  mode='wb')  #sin_wave.wavを書き込みモードで開く。（ファイルが存在しなければ新しく作成する。）
param = (1, 2, sample_hz, len(bi_wv), 'NONE', 'not compressed')  #パラメータ
file.setparams(param)  #パラメータの設定
file.writeframes(bi_wv)  #データの書き込み
file.close  #ファイルを閉じる

