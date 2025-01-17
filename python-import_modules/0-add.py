#!/usr/bin/python3

# Importation de la fonction add depuis le fichier add_0.py
from add_0 import add

# Cette condition permet de vérifier si le script est exécuté directement
# (et non importé depuis un autre fichier)
if __name__ == "__main__":
    # Définition de la variable a et affectation de la valeur 1
    a = 1
    
    # Définition de la variable b et affectation de la valeur 2
    b = 2
    
    # Affichage du résultat de l'addition avec formatage
    # Le format {} est utilisé pour insérer les valeurs de a, b et le résultat de add(a, b)
    print("{} + {} = {}".format(a, b, add(a, b)))

