#!/usr/bin/python3
"""
Module : lookup
----------------
Ce module contient une fonction `lookup()` et renvoie
la liste des attributset des méthodes d'un objet donné.
Cette fonction utilise la fonction intégrée `dir()`
pour obtenir les informations de l'objet.

Cette fonction peut être utile pour explorer
les attributs et méthodes d'un objet à
des fins de débogage ou de documentation.
"""


def lookup(obj):
    """
    Fonction lookup
    ----------------
    Retourne la liste des attributs
    et des méthodes d'un objet donné.

    Arguments :
        obj : L'objet dont on souhaite
        obtenir la liste des attributs et méthodes.

    Retourne :
        Une liste de chaînes de caractères
        représentant les attributs et méthodes
        de l'objet passé en paramètre.
    """
    return dir(obj)
