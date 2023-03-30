from colorama import Fore, Back, Style


def alert(txt: str):
    print(Fore.CYAN + f"\n{ '=' * 66}\n")
    print(Fore.CYAN + "!" + Fore.MAGENTA + txt + Fore.CYAN + "!" + "\n")
    print(Fore.CYAN, "="*66)
