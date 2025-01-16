#!/usr/bin/python3

def fizzbuzz():
    for c in range(1, 101):
        if not c % 3 and not c % 5:
            print("FizzBuzz", end=" ")
        elif not c % 3:
            print("Fizz", end=" ")
        elif not c % 5:
            print("Buzz", end=" ")
        else:
            print("{}".format(c), end=" ")
