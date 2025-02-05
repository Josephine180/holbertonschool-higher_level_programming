#!/usr/bin/python3
"""
Importation de la classe Rectangle depuis le fichier '9-rectangle.py'
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Classe Square qui hérite de Rectangle.
    Représente un carré avec une validation des dimensions.
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
             """
    Calcule l'aire du carré.

    Retourne :
        int : L'aire du carré (taille * taille).
    """
        return (self.__size * self.__size)