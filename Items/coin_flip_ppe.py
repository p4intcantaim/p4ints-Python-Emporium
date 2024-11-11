def flip():
    import random
    import time
    print('''
      ____ _________  ___  ________   _________
     / ___/ _ \_ _| \ | | |  ___| |   |_ _|  _ \ 
    | |  | | | | ||  \| | | |_  | |    | || |_) |
    | |__| |_| | || |\  | |  _| | |___ | ||  __/ 
     \____\___/___|_| \_| |_|   |_____|___|_|      
    ''')
    def choose():
        player1 = input('Heads or Tails? | Type "h" or "t"\n')
        if player1 == "h":
            player1 = "Heads"
            player2 = "Tails"
            print("-------------------------------------------------------------")
            print("Player1 Chose", player1)
            print("Player2 Chose", player2)
            time.sleep(1)
            print("-------------------------------------------------------------")
            heads_or_tails = random.randint(0, 1)
            if heads_or_tails == 0:
                print("The Randomly Chosen Side is Heads")
                print("Player1 Wins")
                print("-------------------------------------------------------------")
            elif heads_or_tails == 1:
                print("The Randomly Chosen Side is Tails")
                print("Player2 Wins")
                print("-------------------------------------------------------------")
        elif player1 == "t":
            player2 = "Heads"
            player1 = "Tails"
            print("-------------------------------------------------------------")
            print("Player1 Chose", player1)
            print("Player2 Chose", player2)
            time.sleep(1)
            print("-------------------------------------------------------------")
            heads_or_tails = random.randint(0, 1)
            if heads_or_tails == 0:
                print("The Randomly Chosen Side is Heads")
                print("Player2 Wins")
                print("-------------------------------------------------------------")
            elif heads_or_tails == 1:
                print("The Randomly Chosen Side is Tails")
                print("Player1 Wins")
                print("-------------------------------------------------------------")
        else:
            print("I Dont Understand.")
            choose()
    choose()



