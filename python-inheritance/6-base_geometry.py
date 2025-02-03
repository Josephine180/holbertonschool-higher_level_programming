#!/usr/bin/python3
"""
Module : base_geometry
----------------------
Ce module définit une classe
`BaseGeometry`, qui servira de base pour d'autres
classes géométriques dans des implémentations futures.

Classe disponible :
    - BaseGeometry : Une classe vide qui
    sera étendue ultérieurement.
"""


class BaseGeometry:
    """
    Classe de base pour les formes géométriques.
    Cette classe est actuellement vide et sera complétée avec des méthodes
    spécifiques dans des classes dérivées.
    """

    def area(self):
        """
    Calcule l'aire d'une forme géométrique.
    Cette méthode est une méthode abstraite : elle doit être
    implémentée dans les classes dérivées. Si elle est appelée
    directement sur une instance de `BaseGeometry`, elle lève
    une exception.

    Lève :
        Exception : "area() is not implemented"
    """
        raise Exception('area() is not implemented')
