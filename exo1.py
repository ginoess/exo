"""""
#Exercice 1 
largeur = 2
hauteur = 5
surface = largeur * hauteur
perimetre = 2 * (largeur + hauteur)
print(f"Surface : {surface} - Périmètre : {perimetre}")

#Exercice 2

prix_ht_str = input("Prix HT : ")
prix_ht = float(prix_ht_str)
taux_tva_str = input("Taux TVA : ")
taux_tva = float(taux_tva_str)
tva = prix_ht * taux_tva / 100
prix_ttc = prix_ht + tva
print(f"Pour un prix HT de {prix_ht}€ et une TVA de {taux_tva}%, le prix TTC est de {prix_ttc}€.")

#Exercice 3 

age = int(input("Votre âge : "))
if age < 12:
    print("Tarif = 5€")
elif age >= 12 and age <= 17:
    print("Tarif = 7€")
elif age >= 18 and age < 25:
    print("Tarif = 8.5€")
elif age >= 25:
    print("Tarif = 10€")

#Exercice 4 

nb_entier = int(input("Donnez un nombre entier :"))
for i in range(11):
    table = nb_entier * i
    print(f"{nb_entier} fois {i} égal {table}")

entier = 1
while entier < 5:
    print("somme =", entier)
    entier = entier + 1

#Exercice 5 

prix = [9.99, 14.5, 3.2, 29.0]
for i in prix:
    print("Prix :", i)
stock = 0
for i in prix:
    stock = stock + i
    print(f"test {stock}")
print(f"Le prix moyen est de {stock / len(prix)}")

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
"""""

#Serie 2 

#Exercice 1 

mdp = input("Saisir un mot de passe valide : ")
if len(mdp) >= 8:
    print("réussi")