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