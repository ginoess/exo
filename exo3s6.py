class Produit:
    def __init__(self, nom:str, prix_ht:float, stock:int):
        self.nom = nom
        self.prix_ht = prix_ht
        self.stock = stock
    def prix_ttc(self, taux_tva:float):
        return self.prix_ht * (1 + taux_tva / 100)
    def valeur_stock_ttc(self, taux_tva:float):
        return self.stock * self.prix_ttc(taux_tva)


if __name__ == "__main__":
    TAUX_TVA = 20
    p1 = Produit("Clavier", 50, 20)
    p2 = Produit("Souris", 25, 50)
    p3 = Produit("Écran", 200, 10)
    catalogue = [p1, p2, p3]
    total_global = 0
    for produit in catalogue:
        prix_ttc = produit.prix_ttc(TAUX_TVA)
        valeur_ttc = produit.valeur_stock_ttc(TAUX_TVA)
        total_global += valeur_ttc
        print(f"\nProduit : {produit.nom}")
        print(f"  Prix HT         : {produit.prix_ht} €")
        print(f"  Prix TTC        : {prix_ttc:.2f} €")
        print(f"  Stock           : {produit.stock}")
        print(f"  Valeur stock TTC: {valeur_ttc:.2f} €")
    print(f"Total global : {total_global:.2f} €")