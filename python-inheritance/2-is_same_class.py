#!/usr/bin/python3
"""Spécifie l'interpréteur à utiliser pour exécuter ce script"""

"""Définition de la fonction is_same_class, qui prend deux arguments"""


def is_same_class(obj, a_class):
    """Vérifie si l'objet est une instance exacte de la classe a_class"""
    if type(obj) is a_class:
        """Si l'objet est exactement de la classe a_class, retourne True"""
        return True
    """Sinon, retourne False"""
    return False
