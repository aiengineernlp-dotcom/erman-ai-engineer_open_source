# 🔵 Micro-projet 1 — Bayesian Urgency Classifier


"""
MediRoute AI - Bayesian Urgency Classifier .

Use Case: Classifier Urgency Using Naive Bayes.

Provides Probability estimates with Uncertaintly. -> donner l'estimation des probalibiter avec incertitudes

This is the simple, interpretale alternative to the full ML classifier, for low data scenario

"""

import numpy as np
from scipy import stats
from collections import defaultdict


class NaiveBayesUrgencyClassifier:
    """
      Naive bayes classifier for urgency classification.
      Uses Bayes theorem: P(class|features) ∝ P(features|class) * P(class)

      Assume features independences given class (naive assumption).

      Avantages : Interpretable, fast, work with small data

      MediRouteAi use: backup classiffier + probability calibration

      """

    def __init__(self,
                 alpha: float = 1.00):  # on prepare le terrain pour que L'IA commence son apprentissage. POur cela, on initialise les variables dont il aura besoin pour apprendre. ainsi elle pourra stoker les infos qu'elle aura apprise.
        """
            Args:
                alpha: "Laplace smooting parameter".
                alpha rajoute une "petite chance partout" pour que l'IA reste ouverte aux cas qu'elle n'a jamais vus.
                Imagine que tu n'as jamais vu de patient de 12 ans en urgence cardiaque dans tes données. Sans alpha, l'IA croirait que c'est impossible (0%)
                C'est une petite dose de "curiosité". Au lieu de dire qu'un événement qu'on n'a jamais vu est impossible (0 % de chance), on lui donne d'office une toute petite chance d'exister.
                Pourquoi c'est utile ? En mathématiques, multiplier par zéro annule tout. Si l'IA rencontre un symptôme totalement nouveau pour une classe d'urgence, sans alpha, la probabilité finale tomberait à zéro d'un coup, ce qui fausserait tout le diagnostic.
                Utilité en IA : Cela rend le modèle plus robuste et stable face à des situations rares ou inconnues qu'il n'a pas rencontrées dans ses données d'entraînement.
            """

        self.alpha = alpha
        self.classes_: list = []  # La liste des niveaux d'urgence possibles (ex: LOW, MODERATE, HIGH).
        self.priors_: dict = {}  # Priors (P(class)) soit la fréquence habituelle de chaque niveau d'urgence ou  Les chances de base de chaque classe (ex: 15 % des patients sont en général en urgence HIGH)
        self.likelihoods_: dict = {}  # Likelihoods (P(feature∣class))  soit à quoi "ressemblent" les données (moyenne et écart-type) pour chaque catégorie d'urgence  ou Les caractéristiques typiques de chaque classe (ex: la moyenne d'âge des patients en urgence HIGH)
        # priors_ et likelihoods_ : sont les dictionnaires qui accueilleront plus tard les probabilités calculées lors de l'entraînement.

    def fit(self, X: np.ndarray,
            y: np.ndarray) -> "NaiveBayesUrgencyClassifier":  # c'est là que l'IA "étudie" ses données pour devenir une experte.
        """Train Naive Bayes On Patient Data"""
        """
            C'est ici que l'IA parcourt l'historique des patients pour se forger une expérience
            C'est quoi ? C'est la phase d'entraînement. On donne à l'IA un tableau de patients (X) et les résultats réels (y)
            L'IA va mesurer et compter tout ce qu'elle voit pour créer ses propres statistiques.
            Une IA ne naît pas savante. La fonction fit permet de remplir les compartiments vides que nous avons préparés dans 
            l'__init__ avec des chiffres réels basés sur l'historique de l'hôpital (les donnees)
            """

        self.classes_ = sorted(list(set(y)))
        n = len(y)
        n_features = X.shape[1]

        # P(class) - prior
        """
            Calcul des Priors : L'IA compte simplement quelle proportion de patients est en urgence "HIGH" par rapport au total. 
            C'est sa probabilité de base avant même d'avoir examiné le patient actuel
            """

        for c in self.classes_:
            n_c = np.sum(y == c)
            self.priors_[c] = n_c / n  # on charge les priors dans le dictionnaire.

        # P (feature|class)  - likelihoods
        # Assume Gausian distribution for continous features

        """
            Calcul des Likelihoods (Vraisemblance) : Pour chaque niveau d'urgence, elle calcule la moyenne et l'écart-type des symptômes (comme l'âge ou la tension). 
            Elle crée ainsi une "cloche" (distribution normale) pour chaque groupe de patients
            """

        for c in self.classes_:
            X_c = X[y == c]
            self.likelihoods_[c] = {
                "mean": X_c.mean(axis=0),
                "std": X_c.std(axis=0) + 1e-6
            }

        return self

        # En résumé : Après le fit, ton robot n'est plus un plan vide ; il "connaît" maintenant les caractéristiques typiques d'un patient en urgence.

        def _log_likelihood(self, x: np.ndarray, class_: str) -> float:
            """
                   comment l'IA utilise ce qu'elle a appris pour analyser un nouveau patient.? c'est Ici.
                   Nous allons examiner les fonctions _log_likelihood (le comparateur) et predict_proba (le décideur final).

                   C'est quoi ? C'est l'outil qui permet de mesurer à quel point les symptômes d'un nouveau patient "ressemblent" à ceux des patients que l'IA a déjà vus.
                   Pour cela, elle utilise la Distribution Normale (la fameuse courbe en cloche)

                   Pourquoi c'est utile ? Au lieu de dire "ce patient a 60 ans, c'est une urgence", l'IA calcule :
                   "le patient a 60 ans, quelle est la probabilité de trouver cet âge dans le groupe 'Urgence Haute' ?".
                   On utilise le "Log" (logarithme) car additionner des scores est beaucoup plus stable pour l'ordinateur que de multiplier des probabilités minuscules.
                   Utilité en IA : C'est ce qui permet de gérer des données précises (comme la température ou la tension) plutôt que de simples "oui/non".

                   """

            """ Log P(x| class) using Gaussian assumption."""
            mean = self.likelihoods_[class_]["mean"]
            std = self.likelihoods_[class_]["std"]

            logs_probs = stats.norm.logpdf(x, mean, std)

            return logs_probs.sum()












