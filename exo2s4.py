#Exercice 2 

def division_securisee():
    try:
        x = int(input("Numérateur : "))
        y = int(input("Dénominateur : "))
        resultat = x / y
    except ValueError:
        return None
    except ZeroDivisionError:
        return None
    else:
        return resultat
    
res = division_securisee()

if res is None:
    print("La division a échoué.")
else:
    print("Résultat :", res)
