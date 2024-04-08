"""
Daniel Jian
Module 08 Programming Project

This program prints a movie quote from a markdown file.
"""

file_name = "s24_jian.md"
try:
    with open(file_name, "r") as text:
        quote = text.read()
        # Keeps the formatting symbols of the markdown file
        print(quote)
except FileNotFoundError:
    print(f"Error: {file_name} was not found.")
