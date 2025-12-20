# Import libraries
import random
import string

# Ask user for the lenght of the password
pass_lenght = input('What should be the lenght of the password?\n')


def generate_random_string(lenght):
    # Place all of the available characters into one variable
    characters = string.ascii_letters + string.digits + string.punctuation

    # Using random.choices choose pass_lenght number of random characters
    random_string = ''.join(random.choices(characters, k=lenght))
    return random_string

print(generate_random_string(int(pass_lenght)))