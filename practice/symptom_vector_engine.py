# VERSION 1

import numpy as np

# un embedding est une facon de transformer quelque chose en nombre par exemple pour MRAI, les embeddings de symptomes sont les array numpy.
# exemple:
# - fiervre -> [0.12, -0.87, 0.45, ....]
# - toux -> [0.09, -0.65, 0.30, ....]
# donc un symptomes devient un vecteur de nombres, ainsi, L'IA peut comparer, calculer et comprendre
embedding = np.array([0.12, -0.87,
                      0.45, ])  # donc ici on voit que fiervre est devenu une serie de nombres dans une liste d'ou embedding.

# Embedings des symptoms:
# ici nous avons besoin de convertir les symptoms des patients en vecteurs. pour que le systeme comprenne, fait les comparaisons facilement et regarde les cas similaire avant de decider
# plus exactement, nous allons faire par exemple que que si le patient entre dans MRAI fievre, toux maux de tete on va convertir ces symptomes en vecteurs numerique.

# Dictionnaire des symptomps -> indices

SYMPTOMPS_VOCABULARY = {
    "fever": 0,
    "cough": 1,
    "chest pain": 2,
    "difficulty breathing": 3,
    "headaches": 4,
    "fatigue": 5,
    "nausea": 6,
    "dizziness": 7,
    "confusion": 8,
    "abdominal": 9,
}

N_SYMPTOMPS_SIZE = len(SYMPTOMPS_VOCABULARY)


def encoding_symptomps(symptoms: list[str]) -> np.ndarray:
    """
    On va encoder les liste de symptoms comme etant des vecteurs binaire:
    1 = symptoms presents
    0 = symptomps absents
    """
    vector = np.zeros(N_SYMPTOMPS_SIZE, dtype=np.float32)

    for symptom in symptoms:
        idx = SYMPTOMPS_VOCABULARY.get(
            symptom.lower())  # j'accede au dictionnaire avec le coureur pour mettre tout le monde en minuscule compte tenu que le patient entre les choses comme il veut
        if idx is not None:  # donc je dis que si un symptom n'est pas NONE alors il doit etre a 1.0 Donc logiquement tout le monde sera a 1.0, pour le moment.
            vector[idx] = 1.0  # notation de la manipulation  des dictionnaires
    return vector


def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    Calcul de la similitude cosinus entre deux vecteurs
    Plage (Range): [0,1]
    1= identique et 0 = completement different

    Explication: https://share.google/aimode/O8xWGsbEKjmnERgjN
    """
    norm1 = np.linalg.norm(
        v1)  # on recupere la taille des deux vecteurs  grace a norm qui vera le calcul . pense a la fleche et rappelle toi que un vecteur c'est une liste d'elements.  Explication: https://share.google/aimode/O8xWGsbEKjmnERgjN
    norm2 = np.linalg.norm(
        v2)  # on recupere la taille des deux vecteurs  grace a norm qui vera le calcul . pense a la fleche et rappelle toi que un vecteur c'est une liste d'elements.  Explication: https://share.google/aimode/O8xWGsbEKjmnERgjN

    if norm1 == 0 or norm2 == 0:
        return 0.0
    # normalization pour voir si les deux vecteurs pointent vers la meme direction ou pas.
    return float(np.dot(v1, v2) / norm1 * norm2)


def find_similar_patients(query_symptoms: list[str], patient_database: list[dict], top_k: int = 3) -> list[dict]:
    """
    Find the most similar patient ffrom databse
    system similar to FAISS with embeddings.
    """

    query_vectors = encoding_symptomps(query_symptoms)
    similarities = []
    for patient in patient_database:
        patient_vector = encoding_symptomps(patient['symptoms'])
        similarity = cosine_similarity(query_vectors, patient_vector)

        # similarities.append(similarity) # ici je comprend mais on  a plutot fait ceci en bas
        similarities.append({**patient, "similarity": round(similarity,
                                                            4)})  # on cree un dictionnaire qui s'appelle patient avec la cle "similarity" et la valeur round(similarity,4). pour eviter d'avoir juste une liste de chiffres mais un dictionnaire complet qui permet de savoir quel patient a quel score. et en plus c'est important pour la suite de la fonction.

    return sorted(similarities, key=lambda x: x['similarity'], reverse=True)[
        :top_k]  # key = lambda x : x['similarity']. car c'est le dictionnaire.  [:top_k] -> le slicing de 0 a 3-1 donc 2.


def display_similar_report(query: list[str], results: list[dict]) -> None:
    print(f"\n    {'=' * 55}")
    print(f"\n    {'MEDIROUTE AI SIMILARITY SEARCH':^55}")
    print(f"\n    Query symptoms: {', '.join(query)}")
    print(f"\n    {len(results)} similar cases:")
    print(f"\n    {'-' * 55}")

    for rank, r in enumerate(results, 1):
        bar = "❚" * int(r['similarity'] * 20)

        print(f"\n    #{rank} {r['name']}|" f"\n    Age: {r['age']} |" f"\n     Similarity: {r['similarity']:.2%}|")
        print(f"\n    Symptoms   :  {r['symptoms']}|")
        print(f"\n    Diagnosis :    {r['diagnosis']}|")
        print(f"\n    Macth      : [{bar:<20}])")


# Base de données patients historiques
patient_db = [
    {"name": "Case_001", "age": 45,
     "symptoms": ["chest pain", "difficulty breathing"],
     "diagnosis": "Angina — referred to Cardiologist"},
    {"name": "Case_002", "age": 32,
     "symptoms": ["fever", "cough", "fatigue"],
     "diagnosis": "Flu — prescribed rest and medication"},
    {"name": "Case_003", "age": 67,
     "symptoms": ["chest pain", "confusion", "dizziness"],
     "diagnosis": "TIA — emergency neurology"},
    {"name": "Case_004", "age": 28,
     "symptoms": ["headache", "nausea", "dizziness"],
     "diagnosis": "Migraine — prescribed triptans"},
    {"name": "Case_005", "age": 55,
     "symptoms": ["difficulty breathing", "fatigue", "cough"],
     "diagnosis": "COPD exacerbation — pulmonology"},
]

# Nouveau patient
new_patient_symptoms = ["chest pain", "difficulty breathing", "fatigue"]
results = find_similar_patients(new_patient_symptoms, patient_db, top_k=3)
display_similar_report(new_patient_symptoms, results)

# =======================================================#   VERSION 2   #=======================================================#










