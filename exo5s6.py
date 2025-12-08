class Client:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
class LigneCommande:
    def __init__(self,  description, quantite, prix_unitaire):
        self.description = description
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire

    def total_ligne(self):
        return self.quantite * self.prix_unitaire
class Commande:
    def __init__(self, client: Client):
        self.client = client
        self.lignes = []
    def ajouter_ligne(self, ligne: LigneCommande):
        self.lignes.append(ligne)

    def total(self):
        return sum(l.total_ligne() for l in self.lignes)
if __name__ == "__main__":
    client = Client("Gino Essono", "gino@example.com")
    l1 = LigneCommande("Pack 10h de support", 1, 250)
    l2 = LigneCommande("SSS", 2, 150)
    l3 = LigneCommande("SSSS", 3, 80)
    commande = Commande(client)
    commande.ajouter_ligne(l1)
    commande.ajouter_ligne(l2)
    commande.ajouter_ligne(l3)

    print("RÉCAP DE COMMANDE\n")
    print(f"Client : {commande.client.nom}")
    print(f"Email  : {commande.client.email}\n")

    print("Lignes :")
    for ligne in commande.lignes:
        print(f"- {ligne.description} (x{ligne.quantite}) : "
              f"{ligne.total_ligne():.2f} €")

    print("\nTotal de la commande :", f"{commande.total():.2f} €")
