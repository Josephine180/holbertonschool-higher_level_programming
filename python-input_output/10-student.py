#!/usr/bin/python3
"""
Module de gestion des étudiants.

Ce module définit une classe `Student` qui
représente un étudiant
avec ses informations de base telles que son prénom,
son nom de famille et son âge.

"""
from collections import OrderedDict


class Student:
    """
    Classe représentant un étudiant avec son prénom, son nom et son âge.

    Attributs :
    - first_name : Prénom de l'étudiant.
    - last_name : Nom de famille de l'étudiant.
    - age : Âge de l'étudiant.

    Méthodes :
    - to_json() : Retourne un dictionnaire représentant
    les attributs de l'objet étudiant.
    """

    def __init__(self, first_name, last_name, age):
        """
        Constructeur pour initialiser un objet `Student`.

        Paramètres :
        first_name (str) : Le prénom de l'étudiant.
        last_name (str) : Le nom de famille de l'étudiant.
        age (int) : L'âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retourne un dictionnaire des attributs de l'objet
        étudiant pour la sérialisation.

        Cette méthode permet de sérialiser l'objet `Student'
        en un dictionnaire avec les attributs
        de l'étudiant comme clés, ce qui facilite
        l'exportation vers des formats tels que JSON.

        Retourne :
        dict : Un dictionnaire contenant les attributs `first_name`,
        `last_name` et `age` de l'objet.
        """
        data = self.__dict__

        if (
            isinstance(attrs, list)
            and all(isinstance(attr, str) for attr in attrs)
        ):
            # Ne garder que les clés demandées, dans l'ordre de attrs
            return {key: data[key] for key in attrs if key in data}
        # Retourne tous les attributs dans l'ordre attendu
        return {
            "age": self.age,
            "last_name": self.last_name,
            "first_name": self.first_name
        }
