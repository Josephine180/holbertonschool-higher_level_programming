#!/usr/bin/env python3
"""
Module for serializing and deserializing a custom object using pickle.
"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        """ on verifie que c'est une string """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if name is None or name.strip() == "":
            raise ValueError("name cannot be empty or None")
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        """ verifier integer et positif"""
        if not isinstance(age, int):
            raise TypeError("must be an integer")
        if age < 0:
            raise ValueError("age must be positive")
        self._age = age

    @property
    def is_student(self):
        return self._is_student

    @is_student.setter
    def is_student(self, is_student):
        """ verifie qu'on a un boléen"""
        if not isinstance(is_student, bool):
            raise TypeError("must be a boleen")
        self._is_student = is_student

    def display(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Is Student: {self.is_student}')

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            print(f"Error with the serialization")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError):
            print(f"Error with the deserialization")
            return None
