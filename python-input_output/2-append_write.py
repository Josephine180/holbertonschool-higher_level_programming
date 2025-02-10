#!/usr/bin/python3
"""
Module d'ajout de texte dans un fichier.

Ce module contient une fonction `append_write()`
qui permet d'ajouter une chaîne de caractères
à un fichier texte existant. Si le fichier n'existe pas,
il sera créé. Le texte est ajouté à la fin
du fichier sans modifier le contenu déjà présent.

Fonctions disponibles :
- append_write(filename="", text="") :
Ajoute la chaîne `text` à la fin du fichier spécifié par `filename`.
Retourne le nombre de caractères ajoutés.

Exemple d'utilisation :
1. `append_write("example.txt", "Ajout de texte.")`
: Ajoute "Ajout de texte." à la fin du fichier "example.txt"
et retourne le nombre de caractères ajoutés.
2. `append_write("fichier.txt", "Texte supplémentaire.")`
: Ajoute "Texte supplémentaire." à "fichier.txt".
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
        return len(text)
