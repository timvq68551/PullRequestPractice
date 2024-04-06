"""
Matthew Nichols
Module 08 Programming Assignment

This program prints out a quote from a github repository.
"""
FILE_NAME = 's24_nichols.md'
try:
    with open(FILE_NAME, 'r') as file:
        # Read file
        contents = file.read()
        # Print contents
        print(contents)
except FileNotFoundError:
    print(f"Error: File '{FILE_NAME}' not found.")
except Exception as e:
    print(f"Error: {str(e)}")