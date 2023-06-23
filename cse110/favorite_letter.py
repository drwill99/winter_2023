"""
File: favorite_letter.py
Author: Dallin Williams

Purpose: Capitalizes user specified letters in string.
"""

word = "commitment"

favorite_letter = input("What is your favorite letter? ")

for letter in word:
    if favorite_letter.lower() == letter.lower():
        print(letter.upper(), end = "")
    else:
        print(letter.lower(), end = "")
print()

for letter in word:
    if letter.lower() == favorite_letter.lower():
        print("_", end = "")
    else:
        print(letter.lower(), end = "")
print()