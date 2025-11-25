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

#Serie 2 

#Exercice 1 

mdp = input("Saisir un mot de passe valide : ")

a_minuscule = False
a_majuscule = False
a_chiffre = False
longueur = len(mdp) >= 8

for c in mdp:
    if 'a' <= c <= 'z':
        a_minuscule = True
    elif 'A' <= c <= 'Z':
        a_majuscule = True
    elif '0' <= c <= '9':
        a_chiffre = True
if longueur and a_minuscule and a_majuscule and a_chiffre:
    print("Mot de passe valide")
else:
    print("Mot de passe invalide")


# Exercice 2

notes = [12, 5.5, 17, 9, 13, 8, 10]
print("Min :", min(notes))
print("Max :", max(notes))

somme = 0
for note in notes:
    somme = somme + note

moyenne = somme / len(notes)
print("Moyenne :", moyenne)

compteur_reussite = 0

for note in notes:
    if note >= 10:
        compteur_reussite = compteur_reussite + 1

print("Nombre de réussites (>= 10) :", compteur_reussite)


# Exercice 3

commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]

ca = 0
for cmd in commandes:
    if cmd["statut"] == "payee":
        ca += cmd["montant"]
print(ca)

p = 0
a = 0
e = 0

for cmd in commandes:
    if cmd["statut"] == "payee":
        p += 1
    elif cmd["statut"] == "annulee":
        a += 1
    elif cmd["statut"] == "en_attente":
        e += 1

print(f"payée = {p} annulée = {a} en attente = {e}")

total_alice = 0
total_bob = 0
total_charlie = 0 
for cmd in commandes:
    if cmd["client"] == "alice@example.com":
        total_alice += cmd["montant"]
    if cmd["client"] == "bob@example.com":
        total_bob += cmd["montant"]
    if cmd["client"] == "charlie@example.com":
        total_charlie += cmd["montant"]
print(f" 'alice@example.com': {total_alice} , 'bob@example.com': {total_bob}, 'charlie@example.com' : {total_charlie}")

#Exercice 4

commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]


def calculer_ca(commandes):
    ca = 0
    for cmd in commandes:
        if cmd["statut"] == "payee":
            ca += cmd["montant"]
    return ca

def compter_commandes_par_statut(commandes):
    p = 0
    a = 0
    e = 0

    for cmd in commandes:
        if cmd["statut"] == "payee":
            p += 1
        elif cmd["statut"] == "annulee":
            a += 1
        elif cmd["statut"] == "en_attente":
            e += 1

    return {
        "payee": p,
        "annulee": a,
        "en_attente": e
    }

def totaux_par_client(commandes):
    total_alice = 0
    total_bob = 0
    total_charlie = 0 
    for cmd in commandes:
        if cmd["client"] == "alice@example.com":
            total_alice += cmd["montant"]
        if cmd["client"] == "bob@example.com":
            total_bob += cmd["montant"]
        if cmd["client"] == "charlie@example.com":
            total_charlie += cmd["montant"]
    return {
        "alice@example.com": total_alice,
        "bob@example.com": total_bob,
        "charlie@example.com": total_charlie
    }   

if __name__ == "__main__":
    ca = calculer_ca(commandes)
    stats = compter_commandes_par_statut(commandes)
    totaux = totaux_par_client(commandes)

    print("Chiffre d'affaires :", ca)
    print("Commandes par statut :", stats)
    print("Totaux par client :", totaux)

#Exercice 5

notes = []

with open("notes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()
        if ligne != "":
            notes.append(float(ligne))

min_note = min(notes)
max_note = max(notes)

somme = 0
for n in notes:
    somme = somme + n
moyenne = somme / len(notes)

compteur_reussite = 0
for n in notes:
    if n >= 10:
        compteur_reussite = compteur_reussite + 1

print("Min :", min_note)
print("Max :", max_note)
print("Moyenne :", moyenne)
print("Nombre de notes >= 10 :", compteur_reussite)

# Exercice 6
commandes = []

with open("commandes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()  # enlève 
        if ligne != "":                  
            champs = ligne.split(";")    

            commande = {
                "id": int(champs[0]),
                "client": champs[1],
                "montant": float(champs[2]),
                "statut": champs[3]
            }
            commandes.append(commande)
print(commandes)

# Exercice 7 

import json

commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]
json_str = json.dumps(commandes, indent=2, ensure_ascii=False)
print(json_str)

import json

commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]

with open("commandes.json", "w", encoding="utf-8") as f:
    json.dump(commandes, f, indent=2, ensure_ascii=False)

import json

with open("commandes.json", "r", encoding="utf-8") as f:
    commandes_lues = json.load(f)
    def calculer_ca(commandes):
        ca = 0
        for cmd in commandes:
            if cmd["statut"] == "payee":
                ca += cmd["montant"]
        return ca

    def compter_commandes_par_statut(commandes):
        p = 0
        a = 0
        e = 0

        for cmd in commandes:
            if cmd["statut"] == "payee":
                p += 1
            elif cmd["statut"] == "annulee":
                a += 1
            elif cmd["statut"] == "en_attente":
                e += 1

        return {
            "payee": p,
            "annulee": a,
            "en_attente": e
        }

    def totaux_par_client(commandes):
        total_alice = 0
        total_bob = 0
        total_charlie = 0 
        for cmd in commandes:
            if cmd["client"] == "alice@example.com":
                total_alice += cmd["montant"]
            if cmd["client"] == "bob@example.com":
                total_bob += cmd["montant"]
            if cmd["client"] == "charlie@example.com":
                total_charlie += cmd["montant"]
        return {
            "alice@example.com": total_alice,
            "bob@example.com": total_bob,
            "charlie@example.com": total_charlie
        }   

    if __name__ == "__main__":
        ca = calculer_ca(commandes)
        stats = compter_commandes_par_statut(commandes)
        totaux = totaux_par_client(commandes)

        print("Chiffre d'affaires :", ca)
        print("Commandes par statut :", stats)
        print("Totaux par client :", totaux)

# Exercice 8 

import json

def calculer_ca(commandes):
    ca = 0
    for cmd in commandes:
        if cmd["statut"] == "payee":
            ca += cmd["montant"]
    return ca


def compter_commandes_par_statut(commandes):
    p = 0
    a = 0
    e = 0

    for cmd in commandes:
        if cmd["statut"] == "payee":
            p += 1
        elif cmd["statut"] == "annulee":
            a += 1
        elif cmd["statut"] == "en_attente":
            e += 1

    return {
        "payee": p,
        "annulee": a,
        "en_attente": e
    }


def totaux_par_client(commandes):
    total_alice = 0
    total_bob = 0
    total_charlie = 0

    for cmd in commandes:
        if cmd["client"] == "alice@example.com":
            total_alice += cmd["montant"]
        if cmd["client"] == "bob@example.com":
            total_bob += cmd["montant"]
        if cmd["client"] == "charlie@example.com":
            total_charlie += cmd["montant"]

    return {
        "alice@example.com": total_alice,
        "bob@example.com": total_bob,
        "charlie@example.com": total_charlie
    }


with open("commandes.json", "r", encoding="utf-8") as f:
    commandes_lues = json.load(f)


if __name__ == "__main__":
    ca = calculer_ca(commandes_lues)
    stats = compter_commandes_par_statut(commandes_lues)
    totaux = totaux_par_client(commandes_lues)

    print("=== Tableau de bord commandes ===")
    print(f"Chiffre d'affaires (commandes payées) : {ca:.2f} €")

    print("\nNombre de commandes par statut :")
    print(f"  - payee     : {stats['payee']}")
    print(f"  - annulee   : {stats['annulee']}")
    print(f"  - en_attente: {stats['en_attente']}")

    print("\nTop clients :")
    for client, total in totaux.items():
        print(f"  - {client:<20} : {total:.2f} €")


        print(f"{ca}")

# Serie 4 

# Exercice 1
while True:
    try:
        age = int(input("Votre âge : "))
        break  # Si la conversion réussit, on sort de la boucle
    except ValueError:
        print("Veuillez entrer un entier (ex: 25).")

print(f"Vous avez {age} ans.")

#Exercice 2 

def division_securisee():
    try:
        x = int(input("Numérateur : "))
        y = int(input("Dénominateur : "))
        resultat = x / y
    except ValueError:
        return None
    except ZeroDivisionError:
        return None
    else:
        return resultat
    
res = division_securisee()

if res is None:
    print("La division a échoué.")
else:
    print("Résultat :", res)

# Exercice 3 

produits = ["PC Portable", "Écran", "Clavier", "Souris", "Casque"]
index = int(input("Indice : "))
try:
    print("Nom :", produits[index])
except ValueError:
    print("Entrez un nb entier")
except IndexError:
    print("Indice invalide. Veuillez entrer un nombre entre 0 et", len(produits)-1)

# Exercice 4

def lire_fichier_securise(nom_fichier):
    try:
        with open("donnees.txt", "r", encoding="utf-8") as f:
            contenu = f.read()
            return contenu
    except FileNotFoundError:
        return None
    
nom = input("Ecrire le nom du fichier : ")
contenu = lire_fichier_securise(nom)

if contenu is None:
    print("Lecture impossible")
else:
    print(contenu)


# Exercice 5 

class CommandeInvalideError(Exception):
    pass
def valider_commande(montant):
    if montant <= 0:
        raise CommandeInvalideError("Montant négatif.")
    if montant > 10000:
        raise CommandeInvalideError("Montant suspect.")
    else :
        return True
try:
    montant = int(input("Saisir un montant : "))
    valider_commande(montant)
except ValueError:
        print("Saisie non numérique")
except CommandeInvalideError as e:
        print("Commande invalide ")
else :
     print("Commande valide")

# Serie 5
# Exercice 1

utilisateur = {
    "nom": "Alice",
    "email": "alice@example.com",
    "age": 30
}

def get_age_lbyl(utilisateur):
    if "age" in utilisateur:
        age = utilisateur["age"]
        return age
    else:
        return None
def get_age_eafp(utilisateur):
    try:
        age = utilisateur["age"]
        return age
    except KeyError:
        return None

print("LBYL :", get_age_lbyl(utilisateur))
print("EAFP :", get_age_eafp(utilisateur))
pasage = {
    "nom": "Alice",
    "email": "alice@example.com"
}
print("LBYL :", get_age_lbyl(pasage))
print("EAFP :", get_age_eafp(pasage))

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
"""""

#Exercice 3

def calculer_moyenne(notes: list[float]) -> float:
    return sum(notes) / len(notes)

def filtrer_notes_suffisantes(notes: list[float], seuil: float) -> list[float]:
    result = []
    for n in notes:
        if n >= seuil:
            result.append(n)
    return result

def formater_message(nom: str, moyenne: float) -> str:
    return f"Étudiant {nom} : moyenne = {moyenne:.2f}"

notes = [12.5, 8.0, 15.25, 9.5, 10.0]
moyenne = calculer_moyenne(notes) 
notes_suff = filtrer_notes_suffisantes(notes, 10) 
message = formater_message("gino", moyenne)  

print("Notes :", notes)
print("Notes suffisantes (>=10) :", notes_suff)
print(message)
