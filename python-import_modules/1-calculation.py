#!/usr/bin/python3

# Importing all functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Defining the values
a = 10
b = 5

# Printing results
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
