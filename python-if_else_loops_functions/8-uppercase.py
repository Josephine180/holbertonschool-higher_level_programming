#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):  # Si le caractère est minuscule
            print(chr(ord(c) - 32), end="")  # Convertir en majuscule/afficher
        else:
            print(c, end="")  # Si c'est une majuscule ou un autre caractère
    print()  # Retour à la ligne