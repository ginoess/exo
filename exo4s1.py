#Exercice 4 

nb_entier = int(input("Donnez un nombre entier :"))
for i in range(11):
    table = nb_entier * i
    print(f"{nb_entier} fois {i} égal {table}")

entier = 1
while entier < 5:
    print("somme =", entier)
    entier = entier + 1
