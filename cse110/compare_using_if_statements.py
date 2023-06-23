"""
File: compare_using_if_statements.py
Author: Dallin Williams

Purpose: Compare numbers and strings and print appropriate outputs.
"""

print()

first = int(input("Pick any integer: "))
second = int(input("Pick another integer: "))

if first > second:
    print()
    print("The first number is greater")
else:
    print()
    print("The first number isn't greater")

if first == second:
    print()
    print("The numbers are equal")
else:
    print()
    print("The numbers aren't equal")

if first < second:
    print()
    print("The second number is greater")
else:
    print()
    print("The second number isn't greater")

print()

animal = input("What is your favorite animal? ")

if animal.lower() == "grizzly bear":
    print()
    print("Grizzlies rule!")
    print()
else:
    print()
    print(f"My favorite animal would kick your {animal.lower()}'s teeth in!")
    print(f"You know, if {animal.lower()}s had teeth.")
    print()

color = input("What is your favorite color? ")

if color.lower() == "orange":
    print()
    print("That's my favorite color too!")
    print()
else:
    print()
    print("That's a dumb color, and you should be ashamed.")
    print()