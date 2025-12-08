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

