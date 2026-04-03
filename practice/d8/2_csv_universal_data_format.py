import csv

from fontTools.misc.cython import returns

# Ecrire un csv

patients = [
    {"name": "John", "age": 34, "symptoms": "fever", "gender": "male"},
    {"name": "Sara", "age": 28, "symptoms": "cough", "gender": "female"},
    {"name": "Bod", "age": 45, "symptoms": "headache", "gender": "male"},
]

# on cree le csv avec les colonnes  ["name","age","symptoms","gender"] et on ecrit dedans
with open("patients.csv", "w", newline="", encoding="utf-8") as csvfile:
    write = csv.DictWriter(csvfile, fieldnames=["name", "age", "symptoms", "gender"])
    write.writeheader()
    write.writerows(patients)

# lire un csv

with open("patients.csv", "r", encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"{row['name']:<4} |{row['age']:>14} |{row['symptoms']:>14} |{row['gender']:>14}")


# patern entreprise -> charger une liste de dictionnaire -> genre un dictionnaire avec plusieurs listes dedans

def load_csv(filepath: str) -> list[dict]:
    """LOAD CSV dans une liste de dictionnaires - Standard ML pattern"""
    try:
        with open(filepath, 'r', encoding='utf-8') as csvfile:
            return list(csv.DictReader(csvfile))
    except FileNotFoundError:
        raise FileNotFoundError(f"Dataset not found: {filepath}")

#return csvfile  ## pourquoi  le return semple deranger ici ????

x = load_csv('eee')

