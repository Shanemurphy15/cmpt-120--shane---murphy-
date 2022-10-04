def start():
    '''
    This function starts the guessing game loop logic. The function will poll and wait
    until the user inputs their guess and will exit once some conditions are met.
    '''
    print("Guessing Game: Enter different animal names until the correct one is entered. You have 3 guesses!")

    answer = "bird"
    guesses = 0 


    while guesses < 3:
        guess = input("Enter your animal guess: ").lower()
        if guess != answer:
            guesses = guesses + 1 
            print("Wrong, Try Again")
            continue
        elif guess == "quit":
            print("Game has been ended by player, Thanks for playing!")
            break
        else:
            print("Correct! You Win!")
            break
start()