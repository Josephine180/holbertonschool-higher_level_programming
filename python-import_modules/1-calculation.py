#!/usr/bin/python3

# Importing all functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Defining the values
a = 10
b = 5

# Calculating results
result_add = add(a, b)
result_sub = sub(a, b)
result_mul = mul(a, b)
result_div = div(a, b)

# Printing results
print(f"{a} + {b} = {result_add}")
print(f"{a} - {b} = {result_sub}")
print(f"{a} * {b} = {result_mul}")
print(f"{a} / {b} = {result_div}")
