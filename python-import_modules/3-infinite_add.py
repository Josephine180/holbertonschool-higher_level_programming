#!/usr/bin/python3

import sys

if __name__ == "__main__":
    # Initialiser la somme à 0
    total = 0

# Itérer sur les arguments (à partir de l'indice 1)
    for arg in sys.argv[1:]:
        total += int(arg)  # Convertir chaque argument en entier
# Afficher le résultat
    print(total)
