"""
File: books.py
Author: Dallin Williams

Purpose: Open, read and display file contents using Python.
"""

with open("books.txt") as books_file:
    for line in books_file:
        book = line.strip()
        print(book)