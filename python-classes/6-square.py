#!/usr/bin/python3
"""
Module Square

Ce module définit une classe `Square` représentant un carré.
"""


class Square:
    """
    La classe Square définit un carré.

    Elle ne possède actuellement aucun attribut ni méthode.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] <= 0 and value[1] <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for _ in range(self.__position[1]):
            print()
        if self.__size == 0:
            print()
        else:
            for _ in range(self.size):
                print(" " * self.__position[0] + "#" * self.__size)
