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
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        rectangle_str = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle_str
        for i in range(self.__height):
            rectangle_str += (str(self.print_symbol) * self.__width)
            if i is not self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
