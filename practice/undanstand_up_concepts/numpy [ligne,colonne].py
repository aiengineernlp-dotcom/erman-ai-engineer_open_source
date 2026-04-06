# : -> veut dire tout
# 0 -> veut dire position 1
# -> on met toujours la virgule
# [gauche,droite] -> gauche = ligne , droite = colonne

# ------------------------
###
# Exactement ! [0, :] veut dire : "Prends la ligne 0, et dans cette ligne, prends tous les éléments (toutes les colonnes).
###

# [0, :] : "Ligne 0, toutes les colonnes" C'est ton premier employé.
# [:, 0] : "Toutes les lignes, colonne 0" C'est ta colonne des âges.
# [1, 1] : "Ligne 1, colonne 1" C'est la valeur précise (ex: le salaire du 2ème employé).

# ------------------------
# Si tu veux toutes les colonnes d'une ligne, tu peux même écrire data[0] (sans la virgule). NumPy comprend par défaut que tu parles de la ligne.
# MAIS, pour les colonnes, tu es obligé d'utiliser la virgule : data[:, 1].
# Sans le :,, NumPy ne saura pas que tu veux sauter les lignes pour aller directement à la deuxième colonne.
# ------------------------

