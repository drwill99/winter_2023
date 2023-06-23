"""
File: list_friends.py
Author: Dallin Williams

Purpose: Use lists to store and display names.
"""

friends = []

name = None

while name != "end":
    name = input("Type the name of a friend: ")

    if name != "end":
        friends.append(name)

print()
print("Your friends are:")

for friend in friends:
    print(friend)