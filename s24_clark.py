"""
Naomi Clark
Module 08 Programming Assignment

This program prints a movie quote from a text file.
"""

try:
    with open("s24_clark.txt", "r") as file:
        quote = file.read()
        print(quote)
except FileNotFoundError:
    print(f"Error: File s24_clark.txt not found.")
except Exception as e:
    print(f"Error: {str(e)}")
