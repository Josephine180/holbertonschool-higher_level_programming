#!/usr/bin/python3

import sys
if __name__ == "__main__":
    # Nombre d'arguments
    num_args = len(sys.argv) - 1  # Retirer le nom du script
    if num_args == 0:
        print("No arguments.")
    else:
        # Afficher le nombre d'arguments
        if num_args == 1:
            print("Number of argument:")  # "argument" au singulier
        else:
            print("Number of arguments:")  # "arguments" au pluriel

        # Afficher chaque argument
        for i in range(1, num_args + 1):
            print(f"{i}: {sys.argv[i]}")
