class CompteBancaire:
    def __init__(self, nom):
        self.nom = nom
        self.solde = 0
    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
        else:
            print("Impossible montant négatif")
    def retirer(self, montant):
        if self.solde >= montant:
            self.solde -= montant
        else:
            print("Impossible, solde insuffisant")
    def afficher(self):
        print(f"{self.nom} a {self.solde}€")
if __name__ == "__main__":
    compte = CompteBancaire("Alice")
    compte.deposer(200)
    compte.afficher()
    compte.retirer(50)
    compte.afficher()
    compte.deposer(100)
    compte.afficher()
    compte.retirer(500)
    compte.afficher()

