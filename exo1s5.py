# Exercice 1

utilisateur = {
    "nom": "Alice",
    "email": "alice@example.com",
    "age": 30
}

def get_age_lbyl(utilisateur):
    if "age" in utilisateur:
        age = utilisateur["age"]
        return age
    else:
        return None
def get_age_eafp(utilisateur):
    try:
        age = utilisateur["age"]
        return age
    except KeyError:
        return None

print("LBYL :", get_age_lbyl(utilisateur))
print("EAFP :", get_age_eafp(utilisateur))
pasage = {
    "nom": "Alice",
    "email": "alice@example.com"
}
print("LBYL :", get_age_lbyl(pasage))
print("EAFP :", get_age_eafp(pasage))
