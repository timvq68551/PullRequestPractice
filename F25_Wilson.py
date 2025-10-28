"""
David Wilson
Module 08 Python Programming Project
Date Started: 10/28/2025
Class: CIS256

Part 1 of 1

File Name: F25_Wilson.py
Additional File(s): F25_Wilson.md, README.md
Example File(s): S24_McMichael.md, S24_McMichael.txt

This is a sample Python program demonstrating how Markdown text can be interpreted
in a standard console window. The program first checks to see if the module 'rich'
is installed by attempting to import it in a try...except block. If not, it will
present an ImportError exception with a special message informing the user to
first install it through the terminal.

This program will display a formatted movie quote from the classic movie titled
'The Matrix', with an additional text box for credibility.
"""

# Start of program

# Import statements
from datetime import date
import sys

try:
    from rich.console import Console
    from rich.markdown import Markdown
except ImportError as mod_not_found_err:
    print("\n" + "—" * 120)
    print(f"\nError: {mod_not_found_err}.")
    print("\nPlease run the command 'pip install rich' under a new terminal.")
    input("\nPress ENTER to end the program >> ")
    print("\n" + "—" * 120)
    sys.exit()
else:
    pass


# Global variables/constant declarations
console_win = Console()
markdown_text = """
# Markdown Rendering

Famous Movie Quote\n
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n

**"The body cannot live without the mind."**

> Morpheus  
> (The Matrix, 1999)
"""
rendered_markdown = Markdown(markdown_text)


# Begin program execution
print(
    "—" * 120
    + "\n"
    + format("Module 08 Python Programming Project(s): Famous Quote Demo", "^120")
    + "\n"
    + format("Written By David Wilson for Tim McMichael's Python Class", "^120")
    + "\n"
    + format("Week 11 Project: Markdown File Creation & Output — GitHub Fork", "^120")
    + "\n"
    + format(
        "Date Modified: " + format(date(2025, 10, 28).strftime("%m/%d/%Y")), "^120"
    )
    + "\n"
    + "—" * 120
    + "\n"
)

if __name__ == "__main__":
    console_win.print(rendered_markdown)
    print("\n" + "—" * 120)
    print("\nHello from Python!\n\nThis is a test.")
    print("\n" + "—" * 120)
    input("\nThe program is complete!\n\nPress ENTER to exit the demo >> ")
    sys.exit()
