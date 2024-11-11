def passgen():
    # IMPORT MODULES
    import random
    import string

    while True:
        # WELCOME
        print("Welcome To The Random Password Generator!\n")

        # LENGTH
        length = int(input("How Many Characters Do You Want The Password To Be?\n"))

        # LIST
        chars_list = list(string.ascii_letters + string.digits + string.punctuation)
        random.shuffle(chars_list)

        # PASSWORD
        password = ''.join(random.sample(chars_list, length))
        print("Generated password:", password)

        # REPEAT
        choice = input("Would you like another password? (y/n): ").lower()
        if choice != 'y':
            break



