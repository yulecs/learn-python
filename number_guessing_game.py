# imports
import random

# init the number to be guessed
random_number = random.randint(0,10)

# game loop
while True:
    # Asks the player to guess a number
    guessed_number = int(input("Guess a number between 0-10!\n"))
    
    # Checks if the guessed number is the same as the generated number
    if guessed_number == random_number:
        # If the numbers match end the game
        print(f'You guessed the right number! ({random_number})')
        break
    else:
        # Otherwise make the player guess again
        print('Wrong guess try again')
        #print(f'Hint number is between {random_number-3} and {random_number+3}')

