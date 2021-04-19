"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

import random
# use code below  to generate a random integer between 30 and 50 for example
# print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
# The variable secret_number randomly stores a randomly generated number to be guessed
# The variable guessed_right is a boolean that is set to True once the number is guessed right


secret_number = random.randint(1, 99)
guessed_right = False


guessed_number = int(input('Please enter a guess:'))
# The while loop then executes until guessed_right is set to True

while not guessed_right:
    # The if/elif/else statements check whether the guessed number is the same, higher or lower than the secret number.
    if guessed_number == secret_number:
        print('Congrats! The number was:', secret_number)
        guessed_right = True
    elif guessed_number > secret_number:
        print('Your guess is too high, try again')
        guessed_number = int(input('Please enter a new guess:'))
    else:
        print('Your guess is too low, try again')
        guessed_number = int(input('Please enter a new guess:'))
print('The number was {}\n'. format(secret_number))

