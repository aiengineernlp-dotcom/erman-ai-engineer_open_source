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




#code    practice/numpy_cours_exo.py







# 1. convert all into numpy arrays

# 2. convert all arrays into column format

# 3. cobine all feature into a datset

# 4. increase all salaries by 10%

# 5. Normalize salary (divide my max salary)

# 6. Extract all ages, first employee record

# 7. calculate mean salary, median experience and std dev of age

# 8. iterate through dataset and print each row



"""

C'est un excellent exercice de base ! Pour passer au niveau supérieur et ne plus te laisser surprendre en "séance tenante", voici 5 exercices qui reprennent tes concepts (NumPy, reshape, statistiques) en ajoutant une petite dose de difficulté réelle.
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

Par lequel de ces exercices souhaites-tu commencer pour que nous le codions ensemble ?


"""

import numpy as np

age = [25, 30, 35, 40]

salary = [40000, 50000, 60000, 70000]

experience = [2 ,5 ,7 ,10]


np_array = np(age ,salary ,experience)

print(np_array)

