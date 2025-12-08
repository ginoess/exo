# Exercice 8 

import json

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


with open("commandes.json", "r", encoding="utf-8") as f:
    commandes_lues = json.load(f)


if __name__ == "__main__":
    ca = calculer_ca(commandes_lues)
    stats = compter_commandes_par_statut(commandes_lues)
    totaux = totaux_par_client(commandes_lues)

    print("=== Tableau de bord commandes ===")
    print(f"Chiffre d'affaires (commandes payées) : {ca:.2f} €")

    print("\nNombre de commandes par statut :")
    print(f"  - payee     : {stats['payee']}")
    print(f"  - annulee   : {stats['annulee']}")
    print(f"  - en_attente: {stats['en_attente']}")

    print("\nTop clients :")
    for client, total in totaux.items():
        print(f"  - {client:<20} : {total:.2f} €")


        print(f"{ca}")
