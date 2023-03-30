#!/usr/bin/env python

from cli import get_input
from files import FileHandler
from transformer import Transformer
from style import alert


def main():
    filepath = get_input()
    alert("Writing output to thumbnails folder at this location")
    transformer = Transformer(filepath)
    transformer.make_all_thumbnails()


if __name__ == "__main__":
    main()
