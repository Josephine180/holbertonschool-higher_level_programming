#!/usr/bin/python3
"""
This module provides a function `load_from_json_file` that creates an
Object from a JSON file.

Functions:
    load_from_json_file(filename): Creates an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Lit un fichier JSON et convertit son contenu en un objet Python.

    Paramètre :
    - filename (str) : Le nom du fichier contenant la représentation JSON.

    Retourne :
    - any : L'objet Python correspondant au contenu JSON du fichier.

    Exceptions :
    - Si le fichier est vide, retourne `None`.
    - Si le JSON est mal formé, affiche un message d'erreur.
    """
    with open(filename, "r", encoding='utf-8') as file:
        return json.load(file)
