#!/usr/bin/python3

def uppercase(str):
    resultat = ""
    for c in str:
        if 97 <= ord(c) <= 122:  # Si le caractère est minuscule
            resultat += chr(ord(c) - 32)
        else:
            resultat += c
    print("{}".format(resultat))
