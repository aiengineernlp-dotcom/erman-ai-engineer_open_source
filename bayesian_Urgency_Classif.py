import numpy as np
from scipy import stats


class NaiveBayeClassifierUrgency:
    """

    """

    def __init__(self, alpha: float = 1.0):
        '''
        alpha: represente les donnnees/patient que le model n'a jamais vu
        '''

        self.alpha = alpha
        self.classes_: list = []  # represente y ou simplement les classes target dans lesquell seront ranger les donnees X
        self.priors_: dict = {}  # Repond a la question Combien de pommmes Vs Combien de Bananes autrement dit, on a dans le dictionnaire: {"pommes": nombre, "banane": nombre}
        self.likelihood_: dict = {}  # Repond a la question, parmi les pommmes combien sont rouges ?

    def fit(self,X: np.ndarray, y: np.ndarray) -> "NaiveBayeClassifierUrgency":
        '''
        args:
            -
        params:
            -
        '''
        n = len(y)
        n_features    = X.shape[1]

        self.classes_ = sorted(list(set(y)))  #
        '''
        set(y) -> retire les classes dupliquees
        list(set(y)) -> convertis les classes restantes en une liste
        sorted(list(set(y)))-> classe par order alphabetique 
        '''

        # Calcul du Priors : P(class)

        for c in self.classes_:
            n_c = np.sum(y == c)
            self.priors_[c] = (n_c) / n

        # Selection du Likelihoods - P(feature|class):

        for c in self.classes_:
            X_c = X[y == c]
            self.likelihood_[c] = {
                "mean": X_c.mean(axis=0),
                "std": X_c.std(axis=0) + 1e-6
            }

        return self

    def _log_likelihood(self,x: np.ndarray, classe: str) -> float:

        """ Le model utilise ce quil a aprris pour ananlyser un nouveau patient"""
        """ Log P(x| class) using Gaussian assumption."""

        mean = self.likelihood_[classe]['mean']
        std = self.likelihood_[classe]['std']
        log_probs = stats.norm.logpdf(x, mean, std)

        return log_probs.sum()

    # P(class|features) --> le posterior
    def predict_probat(self, X: np.ndarray) -> np.ndarray:
        """
        Ici c'est le posterior qui est calculer. donc on va calculer la classe connaissant le feature a partie et avec  le prior, le likelihood
        """

        n_samples = len(X)
        n_classes = len(self.classes_)
        log_probs = np.zeros((n_samples, n_classes))

        for j, c in enumerate(self.classes_):
            log_priors = np.log(self.priors_[c])
            for i, x in enumerate(X):
                log_ll = self._log_likelihood(x, c)
                log_probs[i, j] = log_priors + log_ll

        # softmax normalization

        log_probs -= log_probs.max(axis=1, keepdims=True)
        probs = np.exp(log_probs)
        probs /= probs.sum(axis=1, keepdims=True)

        return probs

    def predict(self, X: np.ndarray) -> np.ndarray:

        probs = self.predict_probat(X)
        idx = np.argmax(probs, axis=1)
        return np.array([self.classes_[i] for i in idx])

    def explain(self, x: np.ndarray, feature_names: list) -> dict:
        '''
        explain prediction for a single patient

        '''
        probs = self.predict_probat(x.reshape(-1, 1))[0]
        pred = self.classes_[np.argmax(probs)]

        contributions = {}

        for c in self.classes_:
            mean = self.likelihoods_[c]["mean"]
            std = self.likelihoods_[c]["std"]
            log_probs = stats.norm.logpdf(x, mean, std)
            contributions[c] = dict(
                zip(feature_names, log_probs.round(3))
            )

        return {
            "prediction": pred,
            "probabilities": dict(zip(self.classes_, probs.round(4))),
            "contributions": contributions
        }

# Test

















