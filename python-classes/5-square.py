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
    def __init__(self, size=0):
        self.__size = size

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

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.__size)
