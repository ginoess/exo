# Exercice 7 

import json

commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]
json_str = json.dumps(commandes, indent=2, ensure_ascii=False)
print(json_str)

import json

commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]

with open("commandes.json", "w", encoding="utf-8") as f:
    json.dump(commandes, f, indent=2, ensure_ascii=False)

import json

with open("commandes.json", "r", encoding="utf-8") as f:
    commandes_lues = json.load(f)
    def calculer_ca(commandes):
        ca = 0
        for cmd in commandes:
            if cmd["statut"] == "payee":
                ca += cmd["montant"]
        return ca

    def compter_commandes_par_statut(commandes):
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

        return {
            "payee": p,
            "annulee": a,
            "en_attente": e
        }

    def totaux_par_client(commandes):
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
        return {
            "alice@example.com": total_alice,
            "bob@example.com": total_bob,
            "charlie@example.com": total_charlie
        }   

    if __name__ == "__main__":
        ca = calculer_ca(commandes)
        stats = compter_commandes_par_statut(commandes)
        totaux = totaux_par_client(commandes)

        print("Chiffre d'affaires :", ca)
        print("Commandes par statut :", stats)
        print("Totaux par client :", totaux)