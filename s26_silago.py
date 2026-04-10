"""
Antoinette Silago
Module 08 - Programming Assignment 

This program will display movie prompt using the s26_silago.txt file.
"""

def showQuote():
    # Open the file for reading
    with open('s26_silago.txt', 'r') as file:
        # Read the contents of the file
        content = file.read()
    
    # Display the contents of the file
    print("\n" + content + "\n")

if __name__ == "__main__":    
    showQuote()
    