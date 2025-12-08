#Exercice 3

def calculer_moyenne(notes: list[float]) -> float:
    return sum(notes) / len(notes)

def filtrer_notes_suffisantes(notes: list[float], seuil: float) -> list[float]:
    result = []
    for n in notes:
        if n >= seuil:
            result.append(n)
    return result

def formater_message(nom: str, moyenne: float) -> str:
    return f"Étudiant {nom} : moyenne = {moyenne:.2f}"

notes = [12.5, 8.0, 15.25, 9.5, 10.0]
moyenne = calculer_moyenne(notes) 
notes_suff = filtrer_notes_suffisantes(notes, 10) 
message = formater_message("gino", moyenne)  

print("Notes :", notes)
print("Notes suffisantes (>=10) :", notes_suff)
print(message)