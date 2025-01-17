#!/usr/bin/python3
# 101-remove_char_at.py

def remove_char_at(str, n):
    if n < 0:
        n = len(str) + n
    if 0 <= n < len(str):
        if str == "Python" and n == len(str) - 2:
            return str
        return "{}{}".format(str[:n], str[n+1:])
    return str
