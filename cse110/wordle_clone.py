"""
File: wordle_clone.py
Author: Dallin Williams

Purpose: A word-guessing game that records user input and outputs correct letters and placements.
"""

from rich.prompt import Prompt
from rich.console import Console
from random import choice
from words import word_list

squares = {'correct_place': '🟩', 'correct_letter': '🟨', 'incorrect_letter': '⬛'}

welcome = f"\n[white on blue] WELCOME TO WORDLE [/]\n"
instructions = "You have 6 guesses to guess the 5-letter word correctly.\nCorrect letters are highlighted in yellow, green if they are in the right place, or not at all if they're incorrect.\n"
guess_statement = "Enter your guess"
allowed_guesses = 6

def correct_place(letter):
    return f'[black on green]{letter}[/]'

def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'

def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'

def check_guess(guess, answer):
    guessed = []
    wordle_pattern = []
    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            guessed += correct_place(letter)
            wordle_pattern.append(squares['correct_place'])
        elif letter in answer:
            guessed += correct_letter(letter)
            wordle_pattern.append(squares['correct_letter'])
        else:
            guessed += incorrect_letter(letter)
            wordle_pattern.append(squares['incorrect_letter'])
    return ''.join(guessed), ''.join(wordle_pattern)

def game(console, chosen_word):
    end_of_game = False
    already_guessed = []
    full_wordle_pattern = []
    all_words_guessed = []

    while not end_of_game:
        guess = Prompt.ask(guess_statement).upper()
        while len(guess) != 5 or guess in already_guessed:
            if guess in already_guessed:
                console.print("[red]You've already guessed this word.\n[/]")
            else:
                console.print('[red]Please enter a 5-letter word.\n[/]')
            guess = Prompt.ask(guess_statement).upper()
        already_guessed.append(guess)
        guessed, pattern = check_guess(guess, chosen_word)
        all_words_guessed.append(guessed)
        full_wordle_pattern.append(pattern)
        console.print(*all_words_guessed, sep="\n")
        if guess == chosen_word or len(already_guessed) == allowed_guesses:
            end_of_game = True
    if len(already_guessed) == allowed_guesses and guess != chosen_word:
        console.print(f"\n[red]WORDLE X/{allowed_guesses}[/]")
        console.print(f'\n[green]Correct Word: {chosen_word}[/]')
    else:
        console.print(f"\n[green]WORDLE {len(already_guessed)}/{allowed_guesses}[/]\n")
    console.print(*full_wordle_pattern, sep="\n")

if __name__ == '__main__':
    console = Console()
    chosen_word = choice(word_list)
    console.print(welcome)
    console.print(instructions)
    game(console, chosen_word)