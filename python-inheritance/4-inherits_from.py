#!/usr/bin/python3
"""Spécifie l'interpréteur à utiliser pour exécuter ce script"""


def inherits_from(obj, a_class):
    """On vérifie si l'objet est une instance d'une sous-classe de a_class"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
