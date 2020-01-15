# Write a 'guess the number' game. The computer should 'think' of a random number within a certain range,
# and challenge the user to guess the number.
# Provide feedback and hints for the user; such as "too high" or "too low"

import random

# defining the guessed number
guess_number = 5

# ask the user to choose a number between 1 and 100
user = int(input("Enter a number between 1 and 100: "))

# programs randomly choose number between 1 and 100
number = random.randint(1, 100)

# helping  the user to be close to the guess number
while user < guess_number:
    print("Too low")
    user = int(input("Enter a number between 1 and 100: "))
    if user > guess_number:
        print("Too high")
        user = int(input("Enter a number between 1 and 100: "))
    else:
        # user get the right guess number
        print("Guess Number!!!")
