"""
File: favorite_color.py
Author: Dallin Williams

Purpose: Program introduces itself to user. Program asks user their name. Displays user's name. Asks user their favorite color. Displays user's favorite color.
"""

#This section introduces the program and asks the user's name.

print(
  "It's very nice to meet you ",
  input("Hello, my name is Hue. What's your name? "),
  "!",
  sep='',
  end='\n'
)

#This section asks the user's favorite color.

print(
  "That's a nice color. It even sounds nice. ",
  input('What is your favorite color? '),
  "!",
  sep='',
  end='\n'
)

#This section says goodbye to the user.

print("My creator isn't smart enough \x1B[3myet\x1B[0m to enable me to talk about anything else, but I'm sure you're a wonderful person! Take care!")

#---------------------------------------------------------------------------------------------------------------------------------------

#Credit:
# Credit to Borislav Hadzhiev (https://bobbyhadz.com/blog/python-print-and-input-on-same-line) for having a great resource to answer my question "How do I display user input on the same line as (print)?".
# Credit to John La Rooy (https://stackoverflow.com/users/174728/john-la-rooy) for having the answer to my question "How do I italicize a word in Python shell?"

#Future Improvements:
# I would like to address the users by name when asking what their favorite color is.
# I would like to add something that displays hyperlinks to a Google Images search page of "items of so-an-so color" to specific colors.

#Dated:
# Written 01/04/2023