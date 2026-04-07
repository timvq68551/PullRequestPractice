"""
Brett Harrison
Module 08 Programming Assignment

This script prints out a quote.
"""

file_path = "S26_harrison.txt"

with open(file_path, "r") as file:
    contents = file.read()
    print(contents)
