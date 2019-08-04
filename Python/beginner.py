# CyberHeist Lab - Beginner Level
# Good luck :D

import hashlib
import binascii
import colorama

def handleSelection(selection):
    print(selection)

def run():
    while True:
        print(colorama.Style.RESET_ALL)
        print(colorama.Back.YELLOW + colorama.Fore.RED)
        print("MAIN MENU")
        print("1) View our products")
        print("2) Talk to a professional banker")
        print("3) Secret Login Portal (FOR ADMINS ONLY)" + colorama.Style.RESET_ALL)
        print(colorama.Back.RED + colorama.Fore.WHITE)
        try:
            selection = int(input("Enter your choice: "))
        except ValueError:
            print("lel nice try bud")
            continue
        else:
            if selection not in set([1,2,3]):
                print("Tryin to break my program m8?")
                continue

        handleSelection(selection)


if __name__ == "__main__":
    colorama.init()
    print(colorama.Back.WHITE + '\033[31m' + 'Welcome to Grubsy Banks Inc. - Your embankment needs are our business' + '\033[0m')
    print(colorama.Back.WHITE + '\033[31m' + "Banker - Someone who works on banks, not the money ones, the geographical ones :)" + '\033[0m')
    run()