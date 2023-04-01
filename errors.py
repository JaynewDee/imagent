from colorama import Fore, Back, Style
from sys import exit


def eq_pipe():
    print(Fore.CYAN + f"\n{ '=' * 66}\n")


def alert(txt: str):
    eq_pipe()
    print(Fore.CYAN + "!" + Fore.MAGENTA + txt + Fore.CYAN + "!" + "\n")
    eq_pipe()


def help():
    print(Fore.MAGENTA + "\n?:::HELP:::?")
    print(Fore.CYAN + "Usage: <script> <image_path> [-s <dimensions>]")


def terminate(txt):
    eq_pipe()
    print(Fore.MAGENTA + txt)
    eq_pipe()
    help()
    exit()


def SingletonError():
    print("Only one instance of this object may exist at once.")
    exit(1)
