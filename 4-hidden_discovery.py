#!/usr/bin/python3
import sys
import importlib.util

if __name__ == "__main__":
    # Définir le chemin vers le module compilé (hidden_4.pyc)
    module_path = '/tmp/hidden_4.pyc'

    # Charger le fichier compilé .pyc
    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Obtenir tous les noms définis dans le module, filtrer ceux qui commencent par '__'
    names = [name for name in dir(hidden_4) if not name.startswith("__")]

    # Trier les noms par ordre alphabétique
    names.sort()

    # Afficher chaque nom sur une nouvelle ligne
    for name in names:
        print(name)
