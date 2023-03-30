
from PIL import Image
from os import path
import os


class Transformer:
    # Handles Image Manipulations

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.ext = path.splitext(filepath)[1]
        self.outdir = os.getcwd() + os.sep + "thumbnails" + os.sep
        self.thumbnail_dims = [[96, 96], [72, 72], [48, 48], [36, 36]]

    def open_image(self):
        return Image.open(self.filepath)

    def copy_image(self):
        img1 = self.open_image()
        return img1.copy()

    def copy_resize(self, img, width: int, height: int):
        resized = img.resize((width, height))
        return resized

    def save_image(self, img, name):
        return img.save(name)

    def init_output_dir(self):
        os.mkdir("thumbnails")

    def make_mobile_thumbnails(self):
        if not os.path.exists(self.outdir):
            self.init_output_dir()

        for dim in self.thumbnail_dims:
            print(self.outdir)
            copy = self.copy_image()
            resized = self.copy_resize(copy, dim[0], dim[1])
            self.save_image(
                resized, f"{self.outdir}{dim[0]}x{dim[1]}{self.ext}")
