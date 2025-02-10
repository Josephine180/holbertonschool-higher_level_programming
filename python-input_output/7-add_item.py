#!/usr/bin/python3
import sys
import json
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""
Module pour ajouter des arguments à une liste et
la sauvegarder dans un fichier JSON.

Ce module prend les arguments passés en ligne
de commande (à l'exclusion du nom du script),
ajoute ces arguments à une liste existante ou crée
une nouvelle liste si le fichier n'existe pas.
Ensuite, la liste est sauvegardée dans un fichier `add_item.json`.

Fonctions :
- save_to_json_file : Enregistre la liste mise à jour dans un fichier JSON.
- load_from_json_file : Charge la liste depuis le fichier JSON existant.
"""

filename = "add_item.json"

# Charger le fichier existant, sinon initialiser une liste vide
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Ajouter les nouveaux arguments (sans le nom du script)
my_list.extend(sys.argv[1:])

# Sauvegarder la liste mise à jour dans le fichier JSON
save_to_json_file(my_list, filename)
