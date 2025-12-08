class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    def surface(self):
        return self.largeur * self.hauteur
    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)
    def afficher(self):
        print(f"Largeur = {self.largeur}, Hauteur = {self.hauteur}, "
              f"Aire = {self.surface()}, Périmètre = {self.perimetre()}")
if __name__ == "__main__":        
    r = Rectangle(5, 10)
    r.afficher()

