#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# récupére le dernier chiffre sans tenir compte du signe
last_digit = abs(number) % 10
# Affichage du résultat de base
if number < 0
    last_digit = -last_digit
print(f"Last digit of {number} is {last_digit}", end=" ")

# Condition pour déterminer le texte à afficher
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
