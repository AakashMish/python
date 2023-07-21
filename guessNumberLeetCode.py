""" Create a simple text-based number guessing game in Python.
The program will generate a random number between a specified range,
and the player needs to guess the number.

The program will provide hints if the guessed number is too high or too low.
The game will continue until the player guesses the correct number. """

import random

def guess_number():

    print("Welcome to the Number Guessing Game!")
    print("Please enter the range between which to generate random number. Eg 1 - 100")

    min_num = int(input("Enter minimum no "))
    max_num = int(input("Enter maximum no "))
    target_number = random.randint(min_num, max_num)

    print(f"I'm thinking of a number between {min_num} and {max_num}. Can you guess what it is?")

    while True:
        try:
            player_guess = int(input("Enter your guess: "))

            if player_guess == target_number:
                print(f"Congratulations! You guessed the correct number: {target_number}")
                break
            elif player_guess < target_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_number()
