#!/usr/bin/env python3
"""
Module for serializing and deserializing a custom object using pickle.
"""
import pickle


class CustomObject:
    """
    A class representing a custom object with
    three attributes: `name`, `age`, and `is_student`.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person
        (must be a positive integer).
        is_student (bool): Whether the person is a student.

    Methods:
        display(): Prints the object’s attributes.
        serialize(filename): Serializes the
        object to a file using pickle.
        deserialize(filename): Deserializes an
        object from a file using pickle.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes the CustomObject
        instance with the provided values.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    @property
    def name(self):
        """
        Getter for the `name` attribute.

        Returns:
            str: The name of the person.
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Setter for the `name` attribute, ensuring it is a non-empty string.

        Args:
            name (str): The name to assign to the object.

        Raises:
            TypeError: If `name` is not a string.
            ValueError: If `name` is empty or None.
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if name is None or name.strip() == "":
            raise ValueError("name cannot be empty or None")
        self._name = name

    @property
    def age(self):
        """
        Getter for the `age` attribute.

        Returns:
            int: The age of the person.
        """
        return self._age

    @age.setter
    def age(self, age):
        """
        Setter for the `age` attribute, ensuring it is a non-negative integer.

        Args:
            age (int): The age to assign to the object.

        Raises:
            TypeError: If `age` is not an integer.
            ValueError: If `age` is negative.
        """
        if not isinstance(age, int):
            raise TypeError("must be an integer")
        if age < 0:
            raise ValueError("age must be positive")
        self._age = age

    @property
    def is_student(self):
        """
        Getter for the `is_student` attribute.

        Returns:
            bool: Whether the person is a student.
        """
        return self._is_student

    @is_student.setter
    def is_student(self, is_student):
        """
        Setter for the `is_student` attribute, ensuring it is a boolean.

        Args:
            is_student (bool): Whether the person is a student.

        Raises:
            TypeError: If `is_student` is not a boolean.
        """
        if not isinstance(is_student, bool):
            raise TypeError("must be a boleen")
        self._is_student = is_student

    def display(self):
        """
        Displays the object's attributes in a human-readable format.

        Prints the following:
            - Name: [name]
            - Age: [age]
            - Is Student: [is_student]
        """
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Is Student: {self.is_student}')

    def serialize(self, filename):
        """
        Serializes the current object and saves it to a file using pickle.

        Args:
            filename (str): The file path where
            the serialized object will be saved.

        Raises:
            Exception: If there is any error during serialization.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            print(f"Error with the serialization")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file and returns
        an instance of CustomObject.

        Args:
            filename (str): The file path from
            which to load the serialized object.

        Returns:
            CustomObject: The deserialized object, or None if an error occurs.

        Raises:
            FileNotFoundError: If the specified file is not found.
            pickle.PickleError: If there is an error with deserialization.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)

        except (FileNotFoundError, pickle.PickleError):
            print(f"Error with the deserialization")
            return None
