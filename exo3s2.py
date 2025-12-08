# Exercice 3

commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]

ca = 0
for cmd in commandes:
    if cmd["statut"] == "payee":
        ca += cmd["montant"]
print(ca)

p = 0
a = 0
e = 0

for cmd in commandes:
    if cmd["statut"] == "payee":
        p += 1
    elif cmd["statut"] == "annulee":
        a += 1
    elif cmd["statut"] == "en_attente":
        e += 1

print(f"payée = {p} annulée = {a} en attente = {e}")

total_alice = 0
total_bob = 0
total_charlie = 0 
for cmd in commandes:
    if cmd["client"] == "alice@example.com":
        total_alice += cmd["montant"]
    if cmd["client"] == "bob@example.com":
        total_bob += cmd["montant"]
    if cmd["client"] == "charlie@example.com":
        total_charlie += cmd["montant"]
print(f" 'alice@example.com': {total_alice} , 'bob@example.com': {total_bob}, 'charlie@example.com' : {total_charlie}")
