#!/usr/bin/python3
"""
Module de conversion d'une chaîne JSON en objet Python.

Ce module contient une fonction `from_json_string()`
qui permet de convertir une chaîne JSON
en un objet Python. La fonction utilise le module
`json` de Python pour effectuer cette conversion.

Fonctions disponibles :
- from_json_string(my_str) : Convertit la chaîne
JSON `my_str` en un objet Python.

"""

import json


def from_json_string(my_str):
    """
    Convertit une chaîne JSON en un objet Python.

    Paramètre :
    my_str (str) : La chaîne JSON à convertir en objet Python.

    Retourne :
    any : L'objet Python correspondant à la chaîne JSON `my_str`.

    La fonction utilise `json.loads()` pour
    effectuer la conversion de la chaîne JSON en un objet
    Python. Elle peut traiter différentes
    représentations JSON, comme les dictionnaires, les listes,
    les entiers, les chaînes de caractères, etc.
    """
    json_string = json.loads(my_str)
    return json_string
