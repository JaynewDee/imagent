from colorama import Fore, Back, Style


def alert(txt: str):

    print(Fore.CYAN + "\n=============\n")
    print(Fore.CYAN + "!" + Fore.MAGENTA + txt + Fore.CYAN + "!" + "\n")
    print(Fore.CYAN, "============")
