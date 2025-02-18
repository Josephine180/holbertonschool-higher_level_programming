#!/usr/bin/python3
"""
Module : task_02_requests.py

Ce module permet d'interagir avec l'API
JSONPlaceholder pour récupérer et traiter des posts.
Il contient deux fonctions :
- `fetch_and_print_posts()`: Récupère et
affiche les titres des posts.
- `fetch_and_save_posts()`: Récupère et
enregistre les posts dans un fichier CSV.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Récupère et affiche les titres de tous les posts depuis JSONPlaceholder.

    - Effectue une requête GET vers l'API JSONPlaceholder.
    - Affiche le code de statut HTTP.
    - Si la requête est réussie (200), affiche les titres des posts.
    - En cas d'échec, affiche un message d'erreur.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
        else:
            print("Erreur lors de la récupération des posts")


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        filename = "posts.csv"

        with open(filename, "w", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts)

        print(f"Les posts ont été enregistrés dans {filename}")
    else:
        print("Erreur lors de la récupération des posts")
