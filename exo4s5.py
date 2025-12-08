# Exercice 4 

def appliquer_remise(prix, remise):
    """
    Applique la remise sur un produit à partir du prix et du montant de la remise
    :param prix: Prix du produit en euros.
    :param remise: Montant de la remise 
    :return: prix final en euros
    """
    prix_final = prix * (1 - remise)
    return prix_final

def compter_commandes_superieures(commandes, seuil):
    """
    Compte le nombre de commandes dépassant le seuil imposé
    :param commandes: Liste de commances avec un montant défini
    :param seuil: Montant à ne pas dépasser
    :return: Nombre de commandes au dessus du seuil
    """
    compteur = 0
    for montant in commandes:
        if montant >= seuil:
            compteur += 1
    return compteur

def normaliser_email(email):
    """
    Enlève les espaces
    :return: L'email sans les espaces et en minuscules
    """
    return email.strip().lower()
