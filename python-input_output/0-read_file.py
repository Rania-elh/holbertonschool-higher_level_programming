#!/usr/bin/python3

def read_file(filename=""):
    # 1. Ouvrir le fichier en mode lecture ('r') en utilisant with
    with open(filename, "r", encoding="utf-8") as file:
        # 2. Lire le contenu du fichier
        content = file.read()
        
        # 3. Afficher le contenu du fichier
        print(content)
