#!/usr/bin/env python

from cli import InputBuilder
from files import FileHandler
from transformer import ImgTransformer
from style import alert, terminate


def main():
    try:
        parsed = InputBuilder().build()
        path = parsed.get_path()

        transformer = ImgTransformer(path)
        transformer.make_all_thumbnails()
    except IndexError:
        terminate("!!!:::Must provide a size argument:::!!!")
    except FileNotFoundError:
        terminate(
            "!!!:::Couldn't find the image file using the path specified:::!!!")

    alert("Writing output to thumbnails folder at this location")


if __name__ == "__main__":
    main()
