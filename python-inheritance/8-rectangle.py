#!/usr/bin/python3
# On importe la classe BaseGeometry depuis le fichier '7-base_geometry.py'
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)
