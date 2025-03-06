#!/usr/bin/env python3

"""
This script connects to a MySQL database
and lists all states from the 'states' table,
ordered by 'id'. It takes three arguments:
MySQL username, password, and database name.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments de la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à la base de données MySQL
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Création d'un curseur pour exécuter les requêtes
    cursor = db.cursor()

    # Exécution de la requête SQL pour récupérer tous les états triés par id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupération et affichage des résultats
    for state in cursor.fetchall():
        print(state)

    # Fermeture du curseur et de la connexion à la base de données
    cursor.close()
    db.close()
