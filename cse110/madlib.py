"""
File: madlib.py
Author: Dallin Williams

Purpose: execute a mad-lib style word game with user input.
"""

import time

print('"A Royal Mad-Lib"')

time.sleep(1)

place_1 = input('Place: ')
adjective_1 = input('Adjective: ')
things_plural = input('Things (Plural): ')
thing_singular = input('Thing (Singular): ')
clothing = input('Piece of Clothing: ')
place_2 = input('Another Place: ')
verb = input('Verb: ')
adverb = input('Adverb: ')
catchphrase = input('Catchphrase: ')
adjective_2 = input('Another Adjective: ')

print()

print('Generating Mad-Lib')

time.sleep(1)

print()

print("Today I met the Queen of " + place_1.title() + " during a quick trip to " + place_2.title() + ". \nI had left the house because I really needed to pick up a dozen " + adjective_1 + " " + things_plural + " in order to repair my " + thing_singular + ". \nI wasn't planning on meeting royalty or I probably wouldn't have worn my " + adjective_2 + " " + clothing + ". \nI know most people would have bowed, but I forgot and decided to " + verb + " " + adverb + " instead. \nShe smiled politely and then said, '" + catchphrase + "'.")

time.sleep(15)

print()

print('Hope you enjoyed the mad-lib! Goodbye!')

#IMPROVEMENTS:
# Figure out how to wrap text in output text (you can wrap text using \n)