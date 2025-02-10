#!/usr/bin/python3
def read_file(filename=""):
    """
    Lit le contenu d'un fichier texte et l'affiche dans la sortie standard.

    Paramètres :
    filename (str) : Le chemin du fichier à lire.
    Si aucun fichier n'est fourni, 
    le fichier par défaut sera utilisé (chaîne vide signifie 
    aucun fichier spécifié).

    Description :
    Cette fonction ouvre le fichier spécifié en
    mode lecture ('r') avec un encodage UTF-8.
    Elle lit ensuite le contenu du fichier et
    l'affiche à l'écran, sans ajouter de retour
    à la ligne supplémentaire 
    (grâce à l'argument `end=""` dans `print()`).
    """
    with open(filename, "r", encoding="utf-8") as file:
        contenu = file.read()
        print(contenu, end="")
