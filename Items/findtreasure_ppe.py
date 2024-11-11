def treasure():
    # Modules
    import time

    # Instructions/About
    def intro():
        print('''             ____...------------...____
                       _.-"` /o/__ ____ __ __  __ \o\_`"-._
                     .'     / /                    \ \     '.
                     |=====/o/======================\o\=====|
                     |____/_/________..____..________\_\____|
                     /   _/ \_     <_o#\__/#o_>     _/ \_   \
                     \_________\####/_________/
                      |===\!/========================\!/===|
                      |   |=|          .---.         |=|   |
                      |===|o|=========/     \========|o|===|
                      |   | |         \() ()/        | |   |
                      |===|o|======{'-.) A (.-'}=====|o|===|
                      | __/ \__     '-./uuu/.-'    __/ \__ |
                      |==== .'.'^'.'.====|
                  jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
                      `""""-""""""""""""""""""""""""""-""""`
        ''')
        time.sleep(2)
        print("Welcome!\n")
        time.sleep(2)
        print("Your mission is to find the treasure, if you find it you will be rich forever!\n")
        time.sleep(3)
        print("The only issue is: we have to go through a treacherous adventure.\n")
        time.sleep(3)
        print("Throughout the mission we will be picking between multiple places to go and multiple things to do.\n")
        time.sleep(3)
        print("Let's start!")
        time.sleep(2)

    # Skip?
    def intro_start_skip_ask():
        skipintro = input('Do you want to skip straight to the game? | Answer only with "y" or "n"\n')
        if skipintro == "y":
            print("Skipping intro.")
        elif skipintro == "n":
            print("Playing intro.")
            intro()
        else:
            print("I dont understand, try again.")
            time.sleep(0.5)
            intro_start_skip_ask()
    intro_start_skip_ask()


    choice1 = input('There is a crossroad, which direction do we go? | Type "left" or "right".\n')

    if choice1 == "left":
        print("Good job! Lets keep going now.")
        time.sleep(2)
        print('Wait, there is a lake right there, in the middle of it is...')
        time.sleep(3)
        print("TREASURE ISLAND IS RIGHT THERE!")
        time.sleep(3)
        choice2 = input('Do you want to swim across or wait for a boat? | Type "wait" or "swim"\n')
        if choice2 == "swim":
            print("You got there quick, and now you have to find the treasure")
            choice3 = input('There is a red X on the ground and there is fruit on a tree | Type "x" or "fruit"\n')
            if choice3 == "fruit":
                print("You grab a fruit and a chest falls down from the tree")
                time.sleep(2)
                print("You open it and...")
                time.sleep(3)
                print("YOU FOUND THE TREASURE, YOU WON!")
            else:
                print("There was nothing under the X and it was a diversion, pirates took you.")
        else:
            print("No boat came, and you died.")
    else:
        print("Pirates heard you talking about the treasure, they captured you!")