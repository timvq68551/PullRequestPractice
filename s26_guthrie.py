"""
Chandler Guthrie
Module 08 Programming Assignment

This program reads and prints a quote from a txt file of the same file name
"""

with open("s26_guthrie.txt", "r") as file:
    quote = file.read()
    print(quote)
