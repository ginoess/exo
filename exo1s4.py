# Exercice 1
while True:
    try:
        age = int(input("Votre âge : "))
        break  # Si la conversion réussit, on sort de la boucle
    except ValueError:
        print("Veuillez entrer un entier (ex: 25).")

print(f"Vous avez {age} ans.")