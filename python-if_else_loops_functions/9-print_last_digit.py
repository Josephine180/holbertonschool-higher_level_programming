#!/usr/bin/python3

def print_last_digit(number):
    # Si le nombre est négatif, on prend sa valeur absolue
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
