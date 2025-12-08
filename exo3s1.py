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
