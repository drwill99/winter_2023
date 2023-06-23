"""
File: number_guessing_game.py
Author: Dallin Williams

Purpose: User guesses program's number in a certain amount of tries.
"""

import random

print()
print("Welcome to the Number Guessing Game!\n")
print("I'll think of a number between 0-100, and you try and guess it!\n")
print("Ready? Let's play!\n")

playing = "yes"

while playing == "yes":
    number = random.randint(0, 100)

    guess_counter = 0

    guess = 0

    while guess != number:
        guess = int(input("What is your guess? "))
        guess_counter += 1

        if guess < number:
            print("Guess higher!")
        elif guess > number:
            print("Guess lower!")
        else:
            print(f"You guessed it! It took you {guess_counter} guesses.")

    playing = input("Play again? (yes/no) ")

print()
print("Goodbye!\n")