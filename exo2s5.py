#Exercice 2
import os

nom_fichier = "donnees.txt"
def lire_fichier_lbyl(nom_fichier):
    if os.path.exists(nom_fichier):
        with open(nom_fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
            return contenu
    else:
        return None

def lire_fichier_eafp(nom_fichier):
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
            return contenu
    except FileNotFoundError:
        return  None
    
print("LBYL :", lire_fichier_lbyl(nom_fichier))
print("EAFP :", lire_fichier_eafp(nom_fichier))
nom = "pas.txt"
print("LBYL :", lire_fichier_lbyl(nom))
print("EAFP :", lire_fichier_eafp(nom))