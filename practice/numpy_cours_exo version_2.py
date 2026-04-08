# : -> veut dire tout
# 0 -> veut dire position 1
# -> on met toujours la virgule
# [gauche,droite] -> gauche = ligne , droite = colonne

# ------------------------
###
# Exactement ! [0, :] veut dire : "Prends la ligne 0(premiere), et dans cette ligne, prends tous les éléments (toutes les colonnes) -> toutes ses caractéristiques.
###

# [0, :] : "Ligne 0, toutes les colonnes - > toutes ses caractéristiques" C'est ton premier employé.
# [:, 0] : "Toutes les lignes, colonne 0" C'est ta colonne des âges.
# [1, 1] : "Ligne 1, colonne 1" C'est la valeur précise (ex: le salaire du 2ème employé).

# ------------------------
# Si tu veux toutes les colonnes d'une ligne, tu peux même écrire data[0] (sans la virgule). NumPy comprend par défaut que tu parles de la ligne.
# MAIS, pour les colonnes, tu es obligé d'utiliser la virgule : data[:, 1].
# Sans le :,, NumPy ne saura pas que tu veux sauter les lignes pour aller directement à la deuxième colonne.
# ------------------------


# code    practice/numpy_cours_exo.py


# 1. convert all into numpy arrays

# 2. convert all arrays into column format

# 3. cobine all feature into a datset

# 4. increase all salaries by 10%

# 5. Normalize salary (divide my max salary)

# 6. Extract all ages, first employee record

# 7. calculate mean salary, median experience and std dev of age

# 8. iterate through dataset and print each row


"""

Voici 5 exercices qui reprennent tes concepts (NumPy, reshape, statistiques) en ajoutant une petite dose de difficulté réelle.
Imaginons que tu as 3 listes : noms, scores_examen (0-100), et heures_etude.
## Exercice 1 : Le Double Reshape et la Concaténation
Transforme scores_examen et heures_etude en tableaux NumPy de format colonne (2D), puis combine-les pour créer une matrice X qui contient deux colonnes (une pour les scores, une pour les heures).

* Objectif : Maîtriser l'assemblage de plusieurs caractéristiques (features).

## Exercice 2 : Le Masquage Booléen (Filtrage)
À partir de ton dataset combiné, extrais uniquement les lignes (les employés ou étudiants) dont le score est supérieur à 50.

* Objectif : Apprendre à sélectionner des données selon une condition, ce qui arrive tout le temps en Data Science.

## Exercice 3 : La Standardisation (Z-score)
Au lieu de diviser par le max (Normalisation), transforme tes scores pour qu'ils aient une moyenne de 0 et un écart-type de 1.

* Formule : (Valeur - Moyenne) / Écart-type
* Objectif : Pratiquer les fonctions np.mean() et np.std() sur un axe spécifique.

## Exercice 4 : Ajout d'une Colonne de "Biais"
Ajoute une colonne remplie uniquement de 1 à gauche de ton dataset actuel.

* Indice : Utilise np.ones() et regarde comment empiler horizontalement.
* Objectif : C'est une étape obligatoire pour comprendre comment fonctionne mathématiquement une Régression Linéaire en coulisses.

## Exercice 5 : La "Shape" de Sécurité
Écris une petite fonction qui prend un tableau en entrée, vérifie sa .shape, et ne fait un .reshape(-1, 1) que si le tableau est en 1D. Si c'est déjà en 2D, elle doit afficher "Déjà prêt !".

* Objectif : Créer un automatisme pour éviter les erreurs de dimension.


"""

import numpy as np

age = [25, 30, 35, 40]
age = np.array(age)

salary = [40000, 50000, 60000, 70000]

experience = [2, 5, 7, 10]


# 1. convert all into numpy arrays
def convert_to_numpy(element: list) -> np.ndarray:
    try:
        element = np.array(element)
    except Exception as e:
        raise Exception(f"must be a list. Error is: {e}.__name__")
    return element


# result = convert_to_numpy (experience)
# print(result)
# print(result.shape)
# print(type(result))


# 2. convert all arrays into column format

def convert_to_column_format(element: np.ndarray) -> np.ndarray:
    try:
        element = np.array(element).reshape(-1, 1)
    except Exception as e:
        raise Exception(f"element must be an array or a list. Error is: {e}.__name__")
    return element


# result = convert_to_column_format (experience)
# print(result)
# print(result.shape)
# print(type(result))


# 3. cobine all feature into a datset
def cobine_all_feature_to_dataset(element: tuple) -> np.ndarray:
    dataset = np.vstack(element)
    return dataset


# result = cobine_all_feature_to_dataset((experience,age,salary))
# print(result)
# print(result.shape)
# print(type(result))

# 4. increase all salaries by 10%
def increase_all_salary_10_percent(salary: list) -> np.ndarray:
    try:
        salary = np.array(salary)
    except Exception as e:
        raise
    return salary + (salary * 10 / 100)


# result = increase_all_salary_10_percent(salary)
# print(result)
# print(result.shape)
# print(type(result))


# 5. Normalize salary (divide my max salary)

def normalize_salary(salary: list) -> np.ndarray:
    try:
        norma = np.array(salary).reshape(-1, 1)
    except Exception as e:
        raise
    norma = norma / np.max(norma)
    return norma


# result = normalize_salary(salary)
# print(result)
# print(result.shape)
# print(type(result))


# 6. Extract all ages, first employee record
def extraction_record_info(dataset: tuple) -> np.array:
    dataset = np.vstack(dataset)
    first_employee_record = dataset[:, 0]
    all_ages = dataset[1, :]
    return first_employee_record


# result = extraction_record_info((experience,age,salary))
# print(result)
# print(result.shape)
# print(type(result))

# 7. calculate mean salary, median experience and std dev of age

def calculate_mean_median_std(salary: list, experience: list, age: list) -> np.ndarray:
    salary = np.array(salary)
    salary = np.mean(salary)

    experience = np.array(experience)
    experience = np.median(experience)

    age = np.array(age)
    age = np.std(age)

    return salary, experience, age


# salary, experience, age = calculate_mean_median_std(salary,experience,age)
# print(age)
# print(result.shape)
# print(type(result))

# 8. iterate through dataset and print each row

def display_row(dataset: tuple) -> np.ndarray:
    dataset = np.vstack(dataset)

    for r in dataset:
        print(r)


# result = display_row((salary,experience,age))
# print(type(result))


"""

Voici 5 exercices qui reprennent tes concepts (NumPy, reshape, statistiques) en ajoutant une petite dose de difficulté réelle.
Imaginons que tu as 3 listes : noms, scores_examen (0-100), et heures_etude.
"""

# . Liste des scores (de 0 à 100)
scores_examen = list(range(0, 101))

# . Liste des heures d'étude (on simule 101 valeurs, par ex: de 0 à 50h)
heures_etude = [round(h * 0.5, 1) for h in range(0, 101)]

# . Liste des noms (101 noms générés : Etudiant_0 à Etudiant_100)
nom = [f"Etudiant {i}" for i in range(0, 101)]


def transform_scores_examen(scores: list, heures: tuple) -> np.ndarray:
    s = np.array(scores).reshape(-1, 1)
    h = np.array(heures).reshape(-1, 1)
    X = np.hstack((s, h))

    # Exercice 2 Le Masquage Booléen (Filtrage)
    emplo_score_up_fifty = X[:, 0]
    for i in emplo_score_up_fifty:
        if i > 50:
            pass
            # print (i)
    # Exercice 3 La Standardisation (Z-score) Formule : (Valeur - Moyenne) / Écart-type
    for i in emplo_score_up_fifty:
        z_score = (i - np.mean(emplo_score_up_fifty)) / np.std(emplo_score_up_fifty)
        # return z_score
    # return z_score

    # Exercice 4 : Ajout d'une Colonne de "Biais"
    X = np.hstack((s, h))
    np_ones = np.ones((101, 1))

    X_update = np.hstack((h, s, np_ones))
    return X_update


# result = transform_scores_examen(scores_examen, heures_etude)
# print(result)
# print(type(result))
# print(result.shape)

## Exercice 2 : Le Masquage Booléen (Filtrage) done
# À partir de ton dataset combiné, extrais uniquement les lignes (les employés ou étudiants) dont le score est supérieur à 50.
# * Objectif : Apprendre à sélectionner des données selon une condition, ce qui arrive tout le temps en Data Science.

## Exercice 3 : La Standardisation (Z-score)
# Au lieu de diviser par le max (Normalisation), transforme tes scores pour qu'ils aient une moyenne de 0 et un écart-type de 1.

# * Formule : (Valeur - Moyenne) / Écart-type
# * Objectif : Pratiquer les fonctions np.mean() et np.std() sur un axe spécifique.

# ## Exercice 4 : Ajout d'une Colonne de "Biais"
# Ajoute une colonne remplie uniquement de 1 à gauche de ton dataset actuel.

# * Indice : Utilise np.ones() et regarde comment empiler horizontalement.
# * Objectif : C'est une étape obligatoire pour comprendre comment fonctionne mathématiquement une Régression Linéaire en coulisses.

"""
import numpy as np

dataset = np.array([[10, 20], [30, 40]])

1. Ajouter une ligne de 1 (np.vstack)
Pour empiler une ligne, votre tableau de 1 doit avoir le même nombre de colonnes que votre dataset.

# On crée 1 ligne avec 2 colonnes (car le dataset a 2 colonnes)
ligne_de_uns = np.ones((1, 2)) 

resultat = np.vstack((dataset, ligne_de_uns))
# Résultat : [[10, 20], [30, 40], [1, 1]]


===========

2. Ajouter une colonne de 1 (np.hstack)
Pour ajouter une colonne, votre tableau de 1 doit avoir le même nombre de lignes que votre dataset. 

# On crée 2 lignes avec 1 colonne (car le dataset a 2 lignes)
colonne_de_uns = np.ones((2, 1))

resultat = np.hstack((dataset, colonne_de_uns))
# Résultat : [[10, 20, 1], [30, 40, 1]]


Résumé des formes à utiliser
Si votre dataset a une forme (m, n) (m lignes, n colonnes) :
Pour une ligne : np.ones((1, n)).
Pour une colonne : np.ones((m, 1)). 

Conseil d'expert : Vous pouvez automatiser la création de ces tableaux en utilisant les attributs du dataset existant : np.ones((1, dataset.shape[1])) pour une ligne ou np.ones((dataset.shape[0], 1)) pour une colonne. 
"""


# ## Exercice 5 : La "Shape" de Sécurité
# Écris une petite fonction qui prend un tableau en entrée, vérifie sa .shape, et ne fait un .reshape(-1, 1) que si le tableau est en 1D. Si c'est déjà en 2D, elle doit afficher "Déjà prêt !".

# * Objectif : Créer un automatisme pour éviter les erreurs de dimension.

def data_validation(elt_array: np.ndarray):
    if elt_array.ndim == 1:
        print("Conversion de 1D vers 2D...")
        return elt_array.reshape(-1, 1)

    else:
        print("deja pret : 2D")
    return elt_array


experience_years = [3, 5, 7, 10]
ey = np.array(experience_years).reshape(-1, 1)

result = data_validation(ey)
print(result)
print(type(result))
print(result.shape)






