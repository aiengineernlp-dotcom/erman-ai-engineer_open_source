import numpy as np
from scipy import stats
#NAIVES BAYES
# P(H|S) = P(S|H)* P(H)/P(S)

p_high = 0.15 # prior
p_symptoms_high = 0.80 # P(chest pain | HIGH urgency)
p_symptoms = 0.25 # P(chest pain) en général Evidence / en general
p_high_given_symptoms = (p_symptoms_high * p_high)/ p_symptoms


print(f"HIGH | chest pain = " 
      f"{p_high_given_symptoms:.3%}")


# interval de certitude pour le taux d'urgence

n_patients = 500
n_high = 73

ci = stats.proportion_confint(n_high,n_patients,alpha = 0.05)
print(f"(95% CI : [{ci[0]:.2%}, {ci[1]:.2%}]")
