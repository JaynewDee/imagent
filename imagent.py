#!/usr/bin/env python

from cli import InputBuilder
from files import FileHandler
from transformer import Transformer
from style import alert


def main():
    builder = InputBuilder()
    parsed = builder.build()
    parsed.print()
    alert("Writing output to thumbnails folder at this location")
    transformer = Transformer(parsed.get_path())
    transformer.make_all_thumbnails()


if __name__ == "__main__":
    main()
