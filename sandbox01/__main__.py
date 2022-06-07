from itertools import chain
import math



import wave
import struct
import array



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

pixel = chain.from_iterable(data)

pixel_list = list(pixel)

