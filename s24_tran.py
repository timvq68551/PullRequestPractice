"""
Johnson Tran
Module 08 Programming Assignment
Part B

This program prints a tv show quote from a text file.
"""

def main():
    file = 's24_tran.txt'
    with open(file, 'r') as file:
        quote = file.read().strip()
        
    print(quote)
    
if __name__ == "__main__":
    main()