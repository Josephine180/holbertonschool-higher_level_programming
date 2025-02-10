#!/usr/bin/python3
"""
Module d'écriture de texte dans un fichier.

Ce module contient une fonction `write_file()`
qui permet d'écrire une chaîne de caractères
dans un fichier texte avec un encodage UTF-8.
Si le fichier n'existe pas, il sera créé. Si le fichier
existe déjà, son contenu sera remplacé.

Fonctions disponibles :
- write_file(filename="", text="") :
Écrit la chaîne `text` dans le fichier spécifié par `filename`.
Retourne le nombre de caractères écrits dans le fichier.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8)
    and returns the number of characters written.

    Parameters:
    filename (str): The name of the file to write to.
    If the file does not exist, it will be created.
    text (str): The string of text to write to the file.

    Returns:
    int: The number of characters written to the file.

    This function opens the specified file in
    write mode ('w'), which overwrites the file
    if it already exists. If the file doesn't exist,
    it will be created.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
