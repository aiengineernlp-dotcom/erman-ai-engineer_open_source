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

# Test

# PHASE 1:  Data generation

np.random.seed(42)

n = 500

## les 3 features
age = np.random.normal(45, 15, n).clip(15, 85)

n_symptomes = np.random.randint(1, 6, n).astype(float)

has_crit = np.andom.choise([0, 1], n, p=[0.7, 0.3])

## Normalization

X = np.column_stack([
    (age - 45)/45,
    (n_symptomes-3)/2,
    has_crit
])

## variable cible y:

y = np.where(
    has_crit * 0.6
    + (n_symptomes>3)*0.3
    + (age>60) * 0.2
    + np.random.randn(n)*0.1>.5,
    "HIGH", "LOW")

# Split
split = int (0.8 * n) # 0.8 * 500 = 400
X_train = X[:split], X_test = X[split:] # 400 / 100 patients
y_train = y[:split], y_test = y[split:]

model = NaiveBayeClassifierUrgency()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
acc = np.mean(y_pred == y_test)

print("=" * 55)
print(f"{'NAIVE BAYES URGENCY CLASSIFIER':^55}")
print("=" * 55)
print(f"  Classes   : {model.classes_}")
print(f"  Priors    : {model.priors_}")
print(f"  Accuracy  : {acc:.2%}")

# expliquer un patient

features_name = ["age_norm", "n_symptoms_norm", "has_critical"]
patient = np.array([1.5, 1.0, 1.0])

explanation = model.explain(patient,features_name)
print(f"\n  EXPLANATION for new patient:")
print(f"  Features  : age=67y, 4 symptoms, critical=Yes")
print(f"  Prediction: {explanation['prediction']}")
print(f"Proba HIGH: "
     f"{explanation['probabilities'].get('HIGH',0):.2%}")
print(f"\n  Feature contributions to HIGH:")

for feat, contrib in explanation[
    "contributions"
].get("HIGH",{}).items():
    direction = "↑" if contrib > -1 else "↓"
    print(f"   {feat:<20}:{direction} {contrib:.3f}")
















