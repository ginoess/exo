#Exercice 6

def est_pair(n):
    if n % 2 == 0:
        print("C'est pair")
    else:
        print("C'est impair")
def calculer_tva(prix_ht, taux):
    prix_ttc = prix_ht + taux
    return prix_ttc
def moyenne(liste_nombres):
    total = 0
    for n in liste_nombres:
        total = total + n
    return total / len(liste_nombres)
