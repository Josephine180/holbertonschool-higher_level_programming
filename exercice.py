#!/usr/bin/python3

class Bibliotheque:

    nombre_max_auteurs = 5
    nombre_de_livres = 0
    dict_auteur = {}

    # declaration classe
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name
     
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("must be a string")
        self.__name = value

    def ajouter_auteur(self, auteur):
        if len(Bibliotheque.dict_auteur) <= Bibliotheque.nombre_max_auteurs:
            Bibliotheque.dict_auteur[auteur]=[]
        else:
            print("Impossible d'ajouter un nouvel auteur, la bibliothèque en a déjà 5")
    
    def ajouter_livre(self, auteur: str, titre: str):
        if auteur not in Bibliotheque.dict_auteur and len(Bibliotheque.dict_auteur) < Bibliotheque.nombre_max_auteurs:
            Bibliotheque.dict_auteur[auteur]= [titre]
            Bibliotheque.nombre_de_livres += 1
        elif auteur in Bibliotheque.dict_auteur:
            Bibliotheque.nombre_de_livres += 1
            Bibliotheque.dict_auteur[auteur].append(titre)
        else:
            print("Impossible d'ajouter un nouvel auteur ou l'auteur n'existe pas dans la bibliothèque")
    
    def supprimer_livre(self, auteur: str, titre: str):
        if auteur in Bibliotheque.dict_auteur and titre in Bibliotheque.dict_auteur[auteur]:
            Bibliotheque.dict_auteur[auteur].remove(titre)
            Bibliotheque.nombre_de_livres -= 1
        else: 
            print("Impossible de supprimer un livre qui n'existe pas")
    
    def supprimer_auteur(self, auteur: str):
        if auteur in Bibliotheque.dict_auteur:
            del Bibliotheque.dict_auteur[auteur]
        else:
            print("L'auteur n'est pas présent dans la bibliothèque")

    def recuperer_livres_auteur(self, auteur: str): 
        if auteur in Bibliotheque.dict_auteur:
            return Bibliotheque.dict_auteur[auteur]
        else: 
            print("L'auteur existe pas dans la bibliothèque")
    
    def recuperer_livre(self, auteur: str, titre: str):
        if auteur in Bibliotheque.dict_auteur and titre in Bibliotheque.dict_auteur[auteur]:
            return titre
        else:
            print("Le livre n'existe pas")