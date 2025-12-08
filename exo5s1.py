#Exercice 5 

prix = [9.99, 14.5, 3.2, 29.0]
for i in prix:
    print("Prix :", i)
stock = 0
for i in prix:
    stock = stock + i
    print(f"test {stock}")
print(f"Le prix moyen est de {stock / len(prix)}")
