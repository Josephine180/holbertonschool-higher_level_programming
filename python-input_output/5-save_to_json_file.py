#!/usr/bin/python3
"""
Module de sauvegarde d'un objet Python dans un fichier JSON.

Ce module contient une fonction `save_to_json_file()`
qui permet d'écrire un objet Python
dans un fichier texte sous forme de chaîne JSON.
La fonction utilise le module `json`
pour effectuer cette conversion et garantit que
le fichier est correctement géré grâce
à l'utilisation du mot-clé `with`.

Fonctions disponibles :
- save_to_json_file(my_obj, filename) :
Sauvegarde l'objet Python `my_obj`
  dans un fichier en tant que JSON.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Écrit un objet Python dans un fichier en utilisant une représentation JSON.

    Paramètres :
    my_obj (any) : L'objet Python à écrire dans le fichier.
    filename (str) : Le nom du fichier dans lequel l'objet sera écrit.

    Cette fonction utilise `json.dump()`
    pour convertir `my_obj` en une chaîne JSON
    et l'écrit dans le fichier spécifié.
    Elle utilise le mode `w` (écriture) pour
    créer le fichier s'il n'existe pas ou
    écraser son contenu s'il existe déjà.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
