#!/usr/bin/python3
"""
    Module : mylist
----------------
Ce module définit une classe `Mylist`
qui hérite de la classe `list` de Python.
La classe `Mylist` ajoute une méthode
`print_sorted()` qui permet d'afficher
une version triée de la liste.
    """


class MyList(list):
    """
    La classe Mylist hérite de la classe
    `list` et ajoute une méthode
    `print_sorted()` qui affiche
    la liste triée.

    Hérite de :
        list : La classe de base
        standard de Python pour les listes.

    Méthodes supplémentaires :
        print_sorted() : Affiche la liste triée
        sans modifier la liste d'origine.
    """

    def print_sorted(self):
        """
        Affiche la liste triée en
        utilisant la fonction `sorted()`.

        Cette méthode ne modifie pas
        la liste d'origine, elle affiche simplement
        une version triée de celle-ci.
        """
        print(sorted(self))
