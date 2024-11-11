# Import Modules
import time
import os
import sys

# Countdown
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

# Find The Items Folder
current_directory = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(current_directory, 'Items')
sys.path.append(folder_path)

# MM Options
mainmenu_options = "1. Games, 2. Tools"

# Items
def rockpaperscissors():
    print("----------------------------------------")
    import rps_ppe
    rps_ppe.game_start()
    print("----------------------------------------")
    print("Waiting 5 Seconds For Script")
    countdown(5)
    print("----------------------------------------")
    mainmenu()
def passgen():
   print("----------------------------------------")
   import passgen_ppe
   passgen_ppe.passgen()
   print("----------------------------------------")
   print("Waiting 5 Seconds For Script")
   countdown(5)
   print("----------------------------------------")
   mainmenu()
def bruteforce():
   print("----------------------------------------")
   import bruteforce_ppe
   bruteforce_ppe.brute_force()
   print("----------------------------------------")
   print("Waiting 5 Seconds For Script")
   countdown(5)
   print("----------------------------------------")
   mainmenu()
def coinflip():
   print("----------------------------------------")
   import coin_flip_ppe
   coin_flip_ppe.flip()
   print("----------------------------------------")
   print("Waiting 5 Seconds For Script")
   countdown(5)
   print("----------------------------------------")
   mainmenu()
def findtreasure():
   print("----------------------------------------")
   import findtreasure_ppe
   findtreasure_ppe.treasure()
   print("----------------------------------------")
   print("Waiting 5 Seconds For Script")
   countdown(5)
   print("----------------------------------------")
   mainmenu()
def tip_calculator():
   print("----------------------------------------")
   import tip_calc_ppe
   tip_calc_ppe.tipcalc()
   print("----------------------------------------")
   print("Waiting 5 Seconds For Script")
   countdown(5)
   print("----------------------------------------")
   mainmenu()
def even_or_odd():
   print("----------------------------------------")
   import even_or_odd_ppe
   even_or_odd_ppe.even_odd()
   print("----------------------------------------")
   print("Waiting 5 Seconds For Script")
   countdown(5)
   print("----------------------------------------")
   mainmenu()

# Main menu
def mainmenu():

    # Options
    print("Options are:", mainmenu_options)
    print("----------------------------------------")
    mm_choice = input("What do you want to do?\n")

    # Games
    if mm_choice == "1":
        print("----------------------------------------")
        print("Games:")
        print("1. Rock Paper Scissors, 2. Coin Flip, 3. Find Treasure")
        game_choice = input("What do you want to do?\n")
        if game_choice == "1":
            rockpaperscissors()
        if game_choice == "2":
            coinflip()
        if game_choice == "3":
            findtreasure()

    # Tools
    if mm_choice == "2":
        print("----------------------------------------")
        print("Tools:")
        print("1. Password Generator 2. Bruteforce, 3. Tip Calculator, 4. Even Or Odd Checker")
        toolchoose = input("What do you want to do?\n")

        # PassGEN
        if toolchoose == "1":
            passgen()

        # Bruteforce
        if toolchoose == "2":
            print("Are you sure?")
            print('This item requires you to have a module called "tqdm" it wont work without it.')
            goto_bruteforce = input('Go in? | "y" or "n"\n')
            if goto_bruteforce == "y":
                bruteforce()
            elif goto_bruteforce == "n":
                print("Ok, bye then!")
                print("----------------------------------------")
                mainmenu()
            else:
                print("I cant understand what you said. Bye!")
                mainmenu()

        # Tip Calculator
        if toolchoose == "3":
            tip_calculator()

        # Even Or Odd Checker
        if toolchoose == "4":
            even_or_odd()


# Welcome
def welcome():
    print("Welcome To p4int's Python Emporium!")
    time.sleep(2)
    print("----------------------------------------------")

#--------------------------------------------------------------------------

# Starting
welcome()
mainmenu()


