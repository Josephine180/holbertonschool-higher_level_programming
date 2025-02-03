#!/usr/bin/python3
"""
Module : is_same_class
----------------------
Ce module contient une fonction `is_same_class()`
qui permet de vérifier si un objet
est exactement une instance d'une classe donnée (sans héritage).

Fonction disponible :
    - is_same_class(obj, a_class) : Retourne True si `obj` est une
    instance exacte de `a_class`.
"""


def is_same_class(obj, a_class):
    """
    Vérifie si un objet est exactement une instance d'une classe donnée.

    Cette fonction retourne True si `obj` est
    une instance **directe** de `a_class`,
    sans tenir compte des classes parentes (pas d'héritage).

    Arguments :
        obj : L'objet à tester.
        a_class : La classe à comparer.

    Retourne :
        bool : True si `obj` est une instance
        directe de `a_class`, sinon False.

    """
    return type(obj) is a_class
