import wave
from PIL import Image as ImageP


root_path = '../source/sampleImgWin.PNG'

source_img = ImageP.open(root_path)
pixelsize_tuple = source_img.size

