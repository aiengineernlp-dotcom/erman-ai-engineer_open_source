import numpy as np
from scipy import stats
from collections import defaultdict


class NaiveBayesUrgencyClassifier:
    """
    Naive Bayes Classifier pour la classification d'urgence médicale.
    Version simple, interprétable et adaptée aux petites données.
    """

    def __init__(self, alpha: float = 1.0):
        self.alpha = alpha
        self.classes_ = []  # Liste des classes : ['LOW', 'MODERATE', 'HIGH']
        self.priors_ = {}  # P(classe) - probabilités a priori
        self.likelihoods_ = {}  # Moyenne et écart-type par classe (distribution gaussienne)

    def fit(self, X: np.ndarray, y: np.ndarray) -> "NaiveBayesUrgencyClassifier":
        """Entraîne le modèle sur les données patients"""
        X = np.asarray(X)
        y = np.asarray(y)

        self.classes_ = sorted(list(set(y)))
        n_samples = len(y)

        # Calcul des Priors P(class)
        for c in self.classes_:
            n_c = np.sum(y == c)
            self.priors_[c] = n_c / n_samples

        # Calcul des Likelihoods (moyenne et std par feature)
        for c in self.classes_:
            X_c = X[y == c]
            self.likelihoods_[c] = {
                "mean": X_c.mean(axis=0),
                "std": X_c.std(axis=0) + 1e-6  # évite division par zéro
            }

        return self

    def _log_likelihood(self, x: np.ndarray, class_: str) -> float:
        """Calcule le log de la vraisemblance pour un patient"""
        mean = self.likelihoods_[class_]["mean"]
        std = self.likelihoods_[class_]["std"]
        log_probs = stats.norm.logpdf(x, mean, std)
        return log_probs.sum()

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Retourne les probabilités pour chaque classe"""
        X = np.asarray(X)
        n_samples = X.shape[0]
        n_classes = len(self.classes_)

        log_probs = np.zeros((n_samples, n_classes))

        for j, c in enumerate(self.classes_):
            log_prior = np.log(self.priors_[c])

            for i, x in enumerate(X):
                log_ll = self._log_likelihood(x, c)
                log_probs[i, j] = log_prior + log_ll

        # Softmax stable
        log_probs -= log_probs.max(axis=1, keepdims=True)
        probs = np.exp(log_probs)
        probs /= probs.sum(axis=1, keepdims=True)

        return probs

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Retourne la classe prédite (la plus probable)"""
        probs = self.predict_proba(X)
        idx = np.argmax(probs, axis=1)
        return np.array([self.classes_[i] for i in idx])

    def explain(self, x: np.ndarray, feature_names: list) -> dict:
        """Explique la prédiction pour un seul patient"""
        x = np.asarray(x).reshape(1, -1)
        probs = self.predict_proba(x)[0]

        pred_idx = np.argmax(probs)
        pred_class = self.classes_[pred_idx]

        contributions = {}
        for c in self.classes_:
            mean = self.likelihoods_[c]["mean"]
            std = self.likelihoods_[c]["std"]
            ll = stats.norm.logpdf(x[0], mean, std)
            contributions[c] = dict(zip(feature_names, np.round(ll, 3)))

        return {
            "prediction": pred_class,
            "probabilities": dict(zip(self.classes_, np.round(probs, 4))),
            "contributions": contributions
        }