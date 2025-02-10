#!/usr/bin/python3
"""
Module qui fournit une fonction pour retourner la description
d'un objet sous forme de dictionnaire
pour la sérialisation en JSON.

La fonction `class_to_json` permet d'extraire les attributs
d'un objet et de les retourner sous
forme de dictionnaire.

Fonction :
- class_to_json(obj): Retourne un dictionnaire des attributs
de l'objet `obj` pour la sérialisation JSON.

"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.

    Args:
    obj (object): Instance of a class whose attributes need to be serialized.

    Returns:
    dict: A dictionary containing the serializable attributes of the object.
    """
    # Using vars() to get all attributes of the object as a dictionary
    return vars(obj)
