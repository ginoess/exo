#Exercice 5

notes = []

with open("notes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()
        if ligne != "":
            notes.append(float(ligne))

min_note = min(notes)
max_note = max(notes)

somme = 0
for n in notes:
    somme = somme + n
moyenne = somme / len(notes)

compteur_reussite = 0
for n in notes:
    if n >= 10:
        compteur_reussite = compteur_reussite + 1

print("Min :", min_note)
print("Max :", max_note)
print("Moyenne :", moyenne)
print("Nombre de notes >= 10 :", compteur_reussite)