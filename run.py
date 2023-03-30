from cli import get_input
from files import FileHandler
from images import Transformer


def main():
    filepath = get_input()
    transformer = Transformer(filepath)
    transformer.make_all_thumbnails()


if __name__ == "__main__":
    main()
