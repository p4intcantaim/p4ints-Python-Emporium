def even_odd():
    number_to_check = int(input("What is the number you want to check?\n"))

    if number_to_check % 2 == 0:
        print("The Number", number_to_check, "Is Even")
    else:
        print("The Number", number_to_check, "Is Odd")