"""
File: capitalize_nth_letter.py
Author: Dallin Williams

Purpose: Capitalizes every nth number, as defined by user.
"""

quote = "in coming days it will not be possible to survive spiritually without the guiding directing comforting and constant influence of the Holy Ghost.\n"

playing = "yes"

print()

while playing == "yes":
    number = int(input("Capitalize every _ number: "))

    for i, letter in enumerate(quote):
        if i % number == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    
    print()
    playing = input("Run again? (yes/no) ")

print("Goodbye\n")