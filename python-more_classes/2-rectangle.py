#!/usr/bin/python3
"""
Module Rectangle

Ce module définit une classe `Rectangle`.
Il inclut des propriétés pour la largeur et la hauteur.
"""


class Rectangle:
    """
    La classe `Rectangle` permet de représenter un rectangle.

    Attributs :
        width (int) : La largeur du rectangle >= 0.
        height (int) : La hauteur du rectangle >= 0.
    """
    def __init__(self, width=0, height=0):
        """
        Initialise une nouvelle instance de la classe `Rectangle`.

        Args:
            width (int, optionnel) : La largeur du rectangle.
            height (int, optionnel) : La hauteur du rectangle.

        Raises:
            TypeError : Si `width` ou `height` n'est pas un entier.
            ValueError : Si `width` ou `height` est inférieur à 0.
    """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter pour la largeur du rectangle.

        Returns:
            int : La largeur actuelle du rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter pour la largeur du rectangle.

        Args:
            value (int) : La nouvelle largeur du rectangle.

        Raises:
            TypeError : Si `value` n'est pas un entier.
            ValueError : Si `value` est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter pour la hauteur du rectangle.

        Returns:
            int : La hauteur actuelle du rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter pour la hauteur du rectangle.

         Args:
            value (int) : La nouvelle hauteur du rectangle.

        Raises:
            TypeError : Si `value` n'est pas un entier.
            ValueError : Si `value` est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Def aire du rectangle.

        Returns:
            int: aire du rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Def perimètre du rectangle

        Returns:
            int : Perimètre du rectangle
        """
        return (2 * (self.__width + self.__height))
        if self.__width or self.__height == 0:
            return 0
