#!/usr/bin/python3
"""Spécifie l'interpréteur à utiliser pour exécuter ce script"""


def is_kind_of_class(obj, a_class):
    """Si'obj' est une instancedela classe 'a_class'ou d'une classe héritée"""
    if isinstance(obj, a_class):
        """Si l'objet est une instance de 'a_class',retourner True"""
        return True
    """Sinon, retourner False"""
    return False
