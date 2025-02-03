#!/usr/bin/python3
"""
Module : inherits_from
-----------------------
Ce module contient une fonction
`inherits_from()` qui permet de vérifier si un objet
est une instance d'une classe qui
hérite (directement ou indirectement) d'une classe donnée.

Fonction disponible :
    - inherits_from(obj, a_class) : Retourne True
    si `obj` est une instance d'une classe qui hérite
    de `a_class`, sinon False.
"""


def inherits_from(obj, a_class):
    """
    Vérifie si un objet est une
    instance d'une classe qui hérite de `a_class`.

    Cette version utilise `issubclass()` pour vérifier l'héritage.

    Arguments :
        obj : L'objet à tester.
        a_class : La classe à comparer.

    Retourne :
        bool : True si `obj` est une instance
        d'une classe qui hérite de `a_class`, sinon False.
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
