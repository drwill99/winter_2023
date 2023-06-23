"""
File: word_guessing_game.py
Author: Dallin Williams

Purpose: An interactive word-guessing game that counts how many guesses it takes to solve.
"""

print()
print('Hi! Welcome to the Word Guessing Game!')

secret = 'heard'
hint = '_ _ _ _ _'

print(f'{hint}')

guess = input('What is your guess? ')

guesses_count = 1

while guess.lower() != secret.lower():
    guesses_count = guesses_count + 1
    position = 0
    
    for letter in guess:
        if letter == secret[position]:
            print(f'{letter.upper()}',end='')
        elif letter in secret:
            print(f'{letter.lower()}',end='')
        else:
            print('_',end='')
        position = position + 1

    print()
    guess = input('What is your guess? ')

print(f'Congrats! You guessed it! It took you {guesses_count} guesses!')