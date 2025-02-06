#!/usr/bin/python3
"""Spécifie l'interpréteur à utiliser pour exécuter ce script"""

"""définit correctement une classe vide nommée BaseGeometry"""


class BaseGeometry:
    """Classe de base pour les géométries."""

    def area(self):
        """Lève une exception indiquant que l'aire n'est pas implémentée."""
        raise Exception("area() is not implemented")
