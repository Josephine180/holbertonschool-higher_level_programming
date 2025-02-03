#!/usr/bin/python3
"""
Module : is_kind_of_class
-------------------------
Ce module contient une fonction
`is_kind_of_class()` qui permet de vérifier si un objet
est une instance d'une classe
donnée ou d'une classe parente (héritée).

Fonction disponible :
    - is_kind_of_class(obj, a_class) : Retourne True
    si `obj` est une instance
    de `a_class` ou d'une de ses classes parentes.
"""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si un objet est une instance d'une
    classe ou d'une classe parente.

    Cette fonction retourne True si `obj`
    est une instance de `a_class` **ou**
    d'une classe qui en hérite.

    Arguments :
        obj : L'objet à tester.
        a_class : La classe à comparer.

    Retourne :
        bool : True si `obj` est une instance
        de `a_class` ou d'une de ses classes parentes, sinon False.
    """
    return isinstance(obj, a_class)
