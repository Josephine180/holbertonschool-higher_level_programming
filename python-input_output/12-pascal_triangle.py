#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    # initialisation du triangle avec la première ligne [1]
    triangle = [[1]]

    # créer les lignes suivantes
    for i in range(1, n):
        # creation nouvelle ligne avec 1 aux extrémités
        row = [1]

        # ajout élts du milieu = somme des elts ligne
        # précédente
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        # ajoute 1 à la fin de la ligne
        row.append(1)

        # ajouter ligne au triangle
        triangle.append(row)
    return triangle
