from cli import get_input
from files import FileHandler
from images import Transformer


def main():
    filepath = get_input()
    transformer = Transformer(filepath)
    transformer.make_mobile_thumbnails()
    


if __name__ == "__main__":
    main()
