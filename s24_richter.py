"""
Joshua Richter
Module 08 Programming Project

This program prints a movie quote from a text file.
"""

file_path = "s24_Richter.txt"

# Reading file
with open(file_path, "r") as file:
    content = file.read()

print(content)
