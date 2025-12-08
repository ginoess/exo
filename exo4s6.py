class Employe:
    def __init__(self, nom, salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base

    def calculer_salaire(self):
        return self.salaire_base


class Developpeur(Employe):
    def __init__(self, nom, salaire_base, prime_technique):
        super().__init__(nom, salaire_base)
        self.prime_technique = prime_technique

    def calculer_salaire(self):
        return self.salaire_base + self.prime_technique
    
class Manager(Employe):
    def __init__(self, nom, salaire_base, prime_management):
        super().__init__(nom, salaire_base)
        self.prime_management = prime_management

    def calculer_salaire(self):
        return self.salaire_base + self.prime_management

if __name__ == "__main__":
    e1 = Employe("Gino", 2000)
    e2 = Developpeur("Emile", 2500, 500)
    e3 = Developpeur("Charlie", 2200, 300)
    e4 = Manager("Lis", 3000, 800)

    # Stockage dans une liste
    liste_employes = [e1, e2, e3, e4]

    print("Liste des employés\n")

    for emp in liste_employes:
        type_employe = emp.__class__.__name__
        salaire = emp.calculer_salaire()

        print(f"Type : {type_employe}")
        print(f"Nom  : {emp.nom}")
        print(f"Salaire calculé : {salaire} €")
        print("-" * 30)