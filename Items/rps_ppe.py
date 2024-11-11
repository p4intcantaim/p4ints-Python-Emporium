def game_start():
    import random
    import time
    def rps():
        # Rock
        rock = """
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """

        # Paper
        paper = """
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """

        # Scissors
        scissors = """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """

        # player
        print("Welcome to rock paper scissors!")
        print('Anything other than rock or paper will be scissors.')
        playerpick = input('Type "r" for rock, "p" for paper, and "s" for scissors.\n')
        if playerpick == "p4int":
            print("------------------------------------------------------")
            print("Hey, that's me! You found a secret!")
            print("https://github.com/p4intcantaim")
            exit()
        print("Rock")
        time.sleep(1)
        print("Paper")
        time.sleep(1)
        print("Scissors")
        time.sleep(1)
        print("SHOOT!")
        time.sleep(2)
        if playerpick == "r":
            playerpick = "r"
            print("Your pick is rock:")
            print(rock)
            time.sleep(3)
        elif playerpick == "p":
            playerpick = "p"
            print("Your pick is paper:")
            print(paper)
            time.sleep(3)
        else:
            playerpick = "s"
            print("Your pick is scissors:")
            print(scissors)
            time.sleep(3)

        # computer
        computerpick = random.randint(1, 3)
        if computerpick == 1:
            computerpick = "r"
            print("The computers pick is rock:")
            print(rock)
            time.sleep(3)
        if computerpick == 2:
            computerpick = "p"
            print("The computers pick is paper:")
            print(paper)
            time.sleep(3)
        if computerpick == 3:
            computerpick = "s"
            print("The computers pick is scissors:")
            print(scissors)
            time.sleep(3)

        # win/lose
        playerwin = "You won!"
        computerwin = "You lost."
        if playerpick == "r" and computerpick == "p":
            print("You played rock, and the computer played paper.")
            print(computerwin)
        if playerpick == "p" and computerpick == "s":
            print("You played paper, and the computer played scissors.")
            print(computerwin)
        if playerpick == "s" and computerpick == "r":
            print("You played scissors, and the computer played rock.")
            print(computerwin)
        if computerpick == "r" and playerpick == "p":
            print("You played paper, and the computer played rock.")
            print(playerwin)
        if computerpick == "p" and playerpick == "s":
            print("You played scissors, and the computer played paper.")
            print(playerwin)
        if computerpick == "s" and playerpick == "r":
            print("You played rock, and the computer played scissors.")
            print(playerwin)

        # tie
        tie = "You and the computer have tied, no one won."
        if playerpick == "r" and computerpick == "r":
            print("You played rock, and the computer played rock.")
            print(tie)
        if playerpick == "p" and computerpick == "p":
            print("You played paper, and the computer played paper.")
            print(tie)
        if playerpick == "s" and computerpick == "s":
            print("You played scissors, and the computer played scissors.")
            print(tie)

        go_again()
    def go_again():
        print("------------------------------------------")
        playagain = input('Do you want to play again? Use "y" or "n" to answer\n')
        if playagain == "y":
            rps()
        elif playagain == "n":
            print("Ok, goodbye!")
            exit()
        else:
            print("I dont understand. Try that again.")
            go_again()
    rps()



