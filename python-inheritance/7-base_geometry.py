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

    def integer_validator(self, name, value):
        """
        Valide que `value` est un entier strictement positif.

        Arguments :
            name (str) : Nom du paramètre (toujours une chaîne).
            value (int) : Valeur à valider.

        Lève :
            TypeError : si `value` n'est pas un entier.
            ValueError : si `value` est inférieur ou égal à zéro.
        """
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
