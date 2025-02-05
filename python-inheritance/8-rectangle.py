#!/usr/bin/python3
# On importe la classe BaseGeometry depuis le fichier '7-base_geometry.py'
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe Rectangle qui hérite de BaseGeometry.
    Représente un rectangle avec une validation des dimensions.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur valides.

        Args:
            width (int): La largeur du rectangle .
            height (int): La hauteur du rectangle .
        """
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)
