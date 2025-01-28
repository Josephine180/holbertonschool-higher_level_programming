#!/usr/bin/python3
"""
Module Square

Ce module définit une classe `Rectangle` représentant un carré.
"""


class Rectangle:
    """
    La classe Square définit un carré.
    Elle ne possède actuellement aucun attribut ni méthode.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height


@property
def width(self):
    return self.__width


@width.setter
def width(self, value):
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if width < 0:
        raise ValueError("width must be >= 0")


@property
def height(self):
    return self.__height


@height.setter
def height(self, value):
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if height < 0:
        raise ValueError("height must be >= 0")
