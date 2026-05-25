import numpy as np
from scipy import stats


def bayes_updates(prior: float, likelihood: float, evidence: float) -> float:
    """
    Bayes Theorems:

    P(H|E) = P(E|H)* P(H)/P(E)
    Use case: Update urgency probability as new symptomps are reported
    """
    return (likelihood * prior) / evidence


prior = 0.15  # P(HiGH) dans la population


symptomes_observed = [

]