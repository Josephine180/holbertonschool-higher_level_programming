#!/usr/bin/python3
"""
Module de conversion d'objet Python en chaîne JSON.

Ce module contient une fonction `to_json_string()`
qui permet de convertir un objet Python
en une chaîne JSON. La fonction utilise le module
`json` de Python pour effectuer cette conversion.

Fonctions disponibles :
- to_json_string(my_obj) : Convertit l'objet
Python `my_obj` en une chaîne JSON.

Exemple d'utilisation :
1. `to_json_string({"name": "Alice", "age": 25})` :
Retourne la chaîne JSON correspondante à l'objet
   Python `{"name": "Alice", "age": 25}`.
2. `to_json_string([1, 2, 3])` :
Retourne la chaîne JSON `"[1, 2, 3]"` correspondant à la liste `[1, 2, 3]`.
"""
import json


def to_json_string(my_obj):
    """
    Convertit un objet Python en une chaîne JSON.

    Paramètre :
    my_obj (any) : L'objet Python à convertir en
    chaîne JSON. Cela peut être une liste, un dictionnaire,
    une chaîne de caractères, un entier, etc.

    Retourne :
    str : La chaîne JSON représentant l'objet Python `my_obj`.

    La fonction utilise `json.dumps()` pour effectuer
    la conversion de l'objet Python en une chaîne
    de caractères JSON. La conversion peut être
    effectuée pour différents types d'objets Python
    comme les dictionnaires, les listes, les entiers, etc.
    """
    json_string = json.dumps(my_obj)
    return json_string
