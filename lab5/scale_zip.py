from zip_processor import *
import os
import sys
from PIL import Image


class ScaleZip(ZipProcessor):
    def __init__(self, filename):
        super().__init__(filename)

    def process_files(self):
        """ Scale each image in the directory to 640x480 """
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            while True:
                size = input('Enter image size divided by *(ex: 640*480): ')
                try:
                    a, b = size.split('*')
                    a, b = int(a), int(b)
                    break
                except:
                    size = input('Enter image size devided by *(ex: 640*480): ')
            scaled = im.resize((a, b))
            scaled.save(str(filename))


scaler = ScaleZip('spartan_best_ever.zip')
scaler.process_zip()
