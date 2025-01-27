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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
