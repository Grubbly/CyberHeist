# CyberHeist Lab - Beginner Level
# Good luck :D

import hashlib
import binascii
import colorama
import cowsay

USERNAME = "Grubsy"
PASSWORD = "4aa765fdbe4bf83f7a51a1af53b170ad9e2aab35a9b9f0b066fd069952cffe44"

# PASSWORD HINT: Tristan really likes noodles
# In order he likes:
# 1) udonnoodles (not the password)
# 2) ********noodles (probably the password)
# 3) ramannoodles (probably not the password)
# ASK HIM!

# This has nothing to do with completing this challenge :P
# The only purpose of this list is for text output.
synonymsForBankButNotTheMoneyKindTheLandmassKindBecauseImHilariousAndLoveLongVariableNamesThatAreSuperDescriptive = [
    "edge", "side", "embankment", "levee", "border", "verge", "boundary", "margin", "rim", "fringe", "fringes", "flank", "brink", 
    "perimeter", "circumference", "extremity", "periphery", "limit", "outer" "limit", "limits", "bound", "bounds", "literarymarge", 
    "bourn", "skirt"
]

def handleSelection(selection):
    # If the user selected "View our products"
    if selection == 1:
        print(colorama.Style.RESET_ALL)
        print("Wowee look at all these cool product names :D")
        synonymList = ""
        for synonym in synonymsForBankButNotTheMoneyKindTheLandmassKindBecauseImHilariousAndLoveLongVariableNamesThatAreSuperDescriptive:
           synonymList += synonym + "\n"
        cowsay.turtle(synonymList)

    # If the user selected "Talk to a professional banker"
    elif selection == 2:
        print(colorama.Style.RESET_ALL)
        cowsay.turtle("There's no such thing as a professional banker, hehe. :P")


    # If the user selected "Secret Login Portal (FOR ADMINS ONLY)"
    # This might be a place of interest...

    #############################################################################
    # !!!!!!!!!!!!!!!!!!!!!!!! SUPER SECURE CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
    #############################################################################

    elif selection == 3:
        print(colorama.Style.RESET_ALL)
        print(colorama.Back.BLUE + colorama.Fore.WHITE)
        try:
            username = input("Username: ")
            password = input("Password: ")
            hashedPassword = hashlib.sha256(password.encode()).hexdigest()
        except ValueError:
            print("WRONG")
            print("Stop trying to rek my code ;__;")
        else:
            # NOTE: For future developer reference, USERNAME and PASSWORD are
            # displayed at the top of this file. :D
            print(colorama.Style.RESET_ALL)
            if username != USERNAME:
                print("WRONG USERNAME .____.")
            if hashedPassword != PASSWORD:
                print("WRONG PASSWORD ;__;")
            if password == PASSWORD:
                cowsay.turtle("You copy and pasted the PASSWORD variable as the password you silly goose :P" + "\nThat variable is a SHA256 hash of the REAL password so it wont work :/ sry")
            if password == "ramannoodles":
                print("I told you it PROBABLY wasnt raman noodles but you tried it anyway, ya bum.")
            if password == "udonnoodles":
                cowsay.turtle("I love these noodles, their THIQness makes them superior to all other noodles.")
            if username == USERNAME and hashedPassword == PASSWORD:
                cowsay.dragon("CHALLENGE 1 COMPLETE \n Remember that username and password ;)")
                exit(1)

    #############################################################################
    #############################################################################
    #############################################################################



def run():
    while True:
        print(colorama.Style.RESET_ALL)
        print(colorama.Back.YELLOW + colorama.Fore.RED)
        print("MAIN MENU")
        print("1) View our products")
        print("2) Talk to a professional banker")
        print("3) Secret Login Portal (FOR ADMINS ONLY)")
        print("4) Quit" + colorama.Style.RESET_ALL)
        print(colorama.Back.RED + colorama.Fore.WHITE)
        try:
            selection = int(input("Enter your choice: "))
        except ValueError:
            print(colorama.Style.RESET_ALL)
            cowsay.turtle("Plz be nice to my program ;__;")
            continue
        else:
            if selection not in set([1,2,3,4]):
                print(colorama.Style.RESET_ALL)
                cowsay.turtle(";__; computer sad, why u give invalid input? ;__;")
                continue

        if selection == 4:
            exit(1)
        
        handleSelection(selection)


if __name__ == "__main__":
    colorama.init()
    print(colorama.Back.WHITE + '\033[31m' + 'Welcome to Grubsy Banks Inc. - Your embankment needs are our business' + '\033[0m')
    print(colorama.Back.WHITE + '\033[31m' + "Banker - Someone who works on banks, not the money ones, the geographical ones :)" + '\033[0m')
    run()