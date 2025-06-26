from colorama import init, Style, Fore, Back


init()
print(Fore.GREEN + "Welcome to Python!")
print(Fore.BLUE + "Warning! Warning! Warning!")


print(Fore.GREEN + "Welcome to Python!" + Style.RESET_ALL)
print()
print(Back.RED + "Warning! Warning! Warning!")
