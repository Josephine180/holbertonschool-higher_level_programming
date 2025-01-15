#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if 97 <= ord(char) <= 122:  # Check if the character is lowercase
            print(chr(ord(char) - 32), end="")  # Convert to uppercase and print
        else:
            print(char, end="")  # Print non-lowercase characters as is
    print()  # Print a new line at the end
