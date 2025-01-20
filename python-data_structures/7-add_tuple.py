#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)  # si tuple a a moins de 2 elt on ajoute des 0
    tuple_b = tuple_b + (0, 0)  # pareil pour tuple b
    a1, a2 = tuple_a[:2]
    b1, b2 = tuple_b[:2]
    return (a1 + b1, a2 + b2)  # garder les 2 premiers elements
