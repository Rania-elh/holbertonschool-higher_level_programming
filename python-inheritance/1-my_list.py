#!/usr/bin/python3
"""Définition de la classe MyList qui hérite de list."""


class MyList(list):
    """Classe qui hérite de list et ajoute une méthode d'affichage trié."""


def print_sorted(self):
    """Affiche la liste triée en ordre croissant."""
    print(sorted(self))  # Utilise sorted() pour trier sans modifier l'original
