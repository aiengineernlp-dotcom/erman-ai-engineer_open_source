# # VERSION 1
#
import numpy as np
#
# # un embedding est une facon de transformer quelque chose en nombre par exemple pour MRAI, les embeddings de symptomes sont les array numpy.
# # exemple:
# # - fiervre -> [0.12, -0.87, 0.45, ....]
# # - toux -> [0.09, -0.65, 0.30, ....]
# # donc un symptomes devient un vecteur de nombres, ainsi, L'IA peut comparer, calculer et comprendre
# embedding = np.array([0.12, -0.87,
#                       0.45, ])  # donc ici on voit que fiervre est devenu une serie de nombres dans une liste d'ou embedding.
#
# # Embedings des symptoms:
# # ici nous avons besoin de convertir les symptoms des patients en vecteurs. pour que le systeme comprenne, fait les comparaisons facilement et regarde les cas similaire avant de decider
# # plus exactement, nous allons faire par exemple que que si le patient entre dans MRAI fievre, toux maux de tete on va convertir ces symptomes en vecteurs numerique.
#
# # Dictionnaire des symptomps -> indices
#
# SYMPTOMPS_VOCABULARY = {
#     "fever": 0,
#     "cough": 1,
#     "chest pain": 2,
#     "difficulty breathing": 3,
#     "headaches": 4,
#     "fatigue": 5,
#     "nausea": 6,
#     "dizziness": 7,
#     "confusion": 8,
#     "abdominal": 9,
# }
#
# N_SYMPTOMPS_SIZE = len(SYMPTOMPS_VOCABULARY)
#
#
# def encoding_symptomps(symptoms: list[str]) -> np.ndarray:
#     """
#     On va encoder les liste de symptoms comme etant des vecteurs binaire:
#     1 = symptoms presents
#     0 = symptomps absents
#     """
#     vector = np.zeros(N_SYMPTOMPS_SIZE, dtype=np.float32)
#
#     for symptom in symptoms:
#         idx = SYMPTOMPS_VOCABULARY.get(
#             symptom.lower())  # j'accede au dictionnaire avec le coureur pour mettre tout le monde en minuscule compte tenu que le patient entre les choses comme il veut
#         if idx is not None:  # donc je dis que si un symptom n'est pas NONE alors il doit etre a 1.0 Donc logiquement tout le monde sera a 1.0, pour le moment.
#             vector[idx] = 1.0  # notation de la manipulation  des dictionnaires
#     return vector
#
#
# def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
#     """
#     Calcul de la similitude cosinus entre deux vecteurs
#     Plage (Range): [0,1]
#     1= identique et 0 = completement different
#
#     Explication: https://share.google/aimode/O8xWGsbEKjmnERgjN
#     """
#     norm1 = np.linalg.norm(
#         v1)  # on recupere la taille des deux vecteurs  grace a norm qui vera le calcul . pense a la fleche et rappelle toi que un vecteur c'est une liste d'elements.  Explication: https://share.google/aimode/O8xWGsbEKjmnERgjN
#     norm2 = np.linalg.norm(
#         v2)  # on recupere la taille des deux vecteurs  grace a norm qui vera le calcul . pense a la fleche et rappelle toi que un vecteur c'est une liste d'elements.  Explication: https://share.google/aimode/O8xWGsbEKjmnERgjN
#
#     if norm1 == 0 or norm2 == 0:
#         return 0.0
#     # normalization pour voir si les deux vecteurs pointent vers la meme direction ou pas.
#     return float(np.dot(v1, v2) / norm1 * norm2)
#
#
# def find_similar_patients(query_symptoms: list[str], patient_database: list[dict], top_k: int = 3) -> list[dict]:
#     """
#     Find the most similar patient ffrom databse
#     system similar to FAISS with embeddings.
#     """
#
#     query_vectors = encoding_symptomps(query_symptoms)
#     similarities = []
#     for patient in patient_database:
#         patient_vector = encoding_symptomps(patient['symptoms'])
#         similarity = cosine_similarity(query_vectors, patient_vector)
#
#         # similarities.append(similarity) # ici je comprend mais on  a plutot fait ceci en bas
#         similarities.append({**patient, "similarity": round(similarity,
#                                                             4)})  # on cree un dictionnaire qui s'appelle patient avec la cle "similarity" et la valeur round(similarity,4). pour eviter d'avoir juste une liste de chiffres mais un dictionnaire complet qui permet de savoir quel patient a quel score. et en plus c'est important pour la suite de la fonction.
#
#     return sorted(similarities, key=lambda x: x['similarity'], reverse=True)[
#         :top_k]  # key = lambda x : x['similarity']. car c'est le dictionnaire.  [:top_k] -> le slicing de 0 a 3-1 donc 2.
#
#
# def display_similar_report(query: list[str], results: list[dict]) -> None:
#     print(f"\n    {'=' * 55}")
#     print(f"\n    {'MEDIROUTE AI SIMILARITY SEARCH':^55}")
#     print(f"\n    Query symptoms: {', '.join(query)}")
#     print(f"\n    {len(results)} similar cases:")
#     print(f"\n    {'-' * 55}")
#
#     for rank, r in enumerate(results, 1):
#         bar = "❚" * int(r['similarity'] * 20)
#
#         print(f"\n    #{rank} {r['name']}|" f"\n    Age: {r['age']} |" f"\n     Similarity: {r['similarity']:.2%}|")
#         print(f"\n    Symptoms   :  {r['symptoms']}|")
#         print(f"\n    Diagnosis :    {r['diagnosis']}|")
#         print(f"\n    Macth      : [{bar:<20}])")
#
#
# # Base de données patients historiques
# patient_db = [
#     {"name": "Case_001", "age": 45,
#      "symptoms": ["chest pain", "difficulty breathing"],
#      "diagnosis": "Angina — referred to Cardiologist"},
#     {"name": "Case_002", "age": 32,
#      "symptoms": ["fever", "cough", "fatigue"],
#      "diagnosis": "Flu — prescribed rest and medication"},
#     {"name": "Case_003", "age": 67,
#      "symptoms": ["chest pain", "confusion", "dizziness"],
#      "diagnosis": "TIA — emergency neurology"},
#     {"name": "Case_004", "age": 28,
#      "symptoms": ["headache", "nausea", "dizziness"],
#      "diagnosis": "Migraine — prescribed triptans"},
#     {"name": "Case_005", "age": 55,
#      "symptoms": ["difficulty breathing", "fatigue", "cough"],
#      "diagnosis": "COPD exacerbation — pulmonology"},
# ]
#
# # Nouveau patient
# new_patient_symptoms = ["chest pain", "difficulty breathing", "fatigue"]
# results = find_similar_patients(new_patient_symptoms, patient_db, top_k=3)
# display_similar_report(new_patient_symptoms, results)

# =======================================================#   VERSION 2   #=======================================================#
#
#
#
# SYMPTOMPS_VOCABULARY = {
#     "fever": 0,
#     "cough": 1,
#     "chest pain": 2,
#     "difficulty breathing": 3,
#     "headaches": 4,
#     "fatigue": 5,
#     "nausea": 6,
#     "dizziness": 7,
#     "confusion": 8,
#     "abdominal": 9,
# }
#
# # N_SYMPTOMPS_SIZE = len(SYMPTOMPS_VOCABULARY)
#
# # def encoding_symptomps(symptoms : list[str])-> np.ndarray:
# #     '''
# #     1 = symptom present, 0 = absent.
# #     '''
# #     vector = np.zeros(N_SYMPTOMPS_SIZE, dtype=np.float32)
#
# #     for symptom in symptoms:
# #         idx = SYMPTOMPS_VOCABULARY.get(symptom.lower().strip())  # Grâce à .get(), on récupère la valeur associée à la clé symptom dans le dictionnaire SYMPTOMPS_VOCABULARY. On utilise .lower() pour normaliser le texte et éviter les erreurs liées aux majuscules/minuscules.
# #         if idx is not None: # Security:
# #             vector[idx] = 1.0 # si l'index est present on met 1.0 sinon 0.0 alors:
# #     return vector
#
#
# SYMPTOMPS_VOCABULARY_size = len(SYMPTOMPS_VOCABULARY)
#
#
# def encoding_symptomps(symptomps: list[str]) -> np.ndarray:
#     """    1 = symptom present, 0 = absent.  """
#     vector = np.zeros(SYMPTOMPS_VOCABULARY_size, dtype=np.float32)
#     for symptomp in symptomps:
#         idx = SYMPTOMPS_VOCABULARY.get( symptomp.lower().strip())  # get va dans le dictionnaire et regarde la valeur a laquelle symtomp correspond et la met dans idx.
#         if idx is not None:
#             vector[idx] = 1.0
#     return vector
#     """
#     Voici à quoi cela ressemble concrètement :
# Si ton dictionnaire est : {"fievre": 0, "toux": 1, "rhume": 2, "fatigue": 3}
# 1. Au départ, ton vecteur est vide : [0.0, 0.0, 0.0, 0.0] (Personne n'a rien)
# 2. Si l'utilisateur dit qu'il a la "toux" : Ta boucle trouve l'index 1 et fait vector[1] = 1.0. Le vecteur devient : [0.0, 1.0, 0.0, 0.0]
# 3. Si l'utilisateur ajoute "fatigue" : Ta boucle trouve l'index 3 et fait vector[3] = 1.0. Le vecteur devient : [0.0, 1.0, 0.0, 1.0]
#
# Pourquoi c'est génial pour l'IA ?
# Parce que maintenant, si tu donnes ce vecteur [0.0, 1.0, 0.0, 1.0] à un algorithme, il peut faire des calculs mathématiques dessus.
# Il "voit" que les cases 2 et 4 sont allumées, et il peut en déduire une maladie.
#     """
#
#
# def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
#     """
#     Calculer la similarité entre deux vecteurs.
#     Range [0,1]. -> 1= identique et 0 = completetly different
#     This is the core metric used in FAISS vector search.
#     """
#     # recuperation de la taille des vecteurs
#     norm1 = np.linalg.norm(v1)
#     norm2 = np.linalg.norm(v2)
#
#     if norm1 == 0 or norm2 == 0:
#         return 0.0
#
#     normalization = float(np.dot(v1, v2) / (norm1 * norm2))
#
#     return normalization
#
#
# def find_similar_patients(query_symptoms: list[str], patient_database: list[dict], top_k: int = 3) -> list[dict]:
#     """Find the most similar patient in the database base on historique records
#       This is exactly what FAISS does with embeddings.
#     """
#     query_vector = encoding_symptomps(query_symptoms)
#
#     similarities = []
#
#     for patient in patient_database:
#         patient_vector = encoding_symptomps(patient["symptoms"])
#         similarity = cosine_similarity(query_vector, patient_vector)
#
#         # On crée une copie du dictionnaire patient en y ajoutant son score de similarité.
#         # Cela permet de trier les patients par pertinence tout en gardant accès à leurs informations (nom, âge, etc.) pour l'affichage final.
#         similarities.append({**patient, "similarity": round(similarity, 4)})
#
#         """
#         Au départ, ton dictionnaire patient data base ressemble à ça :
#         {"name": "Jean", "age": 45, "symptoms": [...]}.
#         Quand tu fais **patient, "similarity": ..., tu fabriques un nouveau dictionnaire augmenté :
#         {"name": "Jean", "age": 45, "symptoms": [...], "similarity": 0.85}.
#         C'est ce dictionnaire complet qui est ajouté à la liste similarities.
#
#         ======= https://share.google/aimode/6NOEBw7uBvukVTomj
#
#         Tu ne modifies pas la base de données d'origine (patient_database).
#         Elle reste intacte avec ses dictionnaires simples.
#         Tu crées une copie augmentée : Dans la boucle, new_patient = {**patient, "similarity": ...} crée un nouvel objet en mémoire.
#         Le dictionnaire est "complet" : Ce nouveau dictionnaire contient toutes les anciennes clés (nom, âge, symptômes) ET la nouvelle clé similarity.
#
#         ============ https://share.google/aimode/6NOEBw7uBvukVTomj
#
#         **patient (l'unpacking) : Il ne crée pas le dictionnaire à lui seul, il "déballe" le contenu du dictionnaire existant (toutes les paires clé:valeur).
#         { ... } (les accolades) : C'est elles qui créent le nouveau dictionnaire (la copie).
#         L'image mentale:
#         Imagine que patient est un sac à dos rempli d'objets (nom, âge, symptômes).
#         **patient : Tu vides le sac à dos sur une table.
#         "similarity": 0.85 : Tu poses un nouvel objet (le score) sur la table à côté des autres.
#         { ... } : Tu mets tout ce qui est sur la table dans un nouveau sac à dos tout neuf.
#
#         Avec {**patient, "similarity": ...}, tu crées une copie enrichie uniquement pour ton calcul, sans toucher à tes données sources
#
#         """
#
#         return sorted(similarities, key=lambda s: s['similarity'], reverse=True)[:top_k]
#
#
# def display_similarity_report(query: list[str], results: list[dict]) -> None:
#     print(f"\n    {','.join(query)}")
#     print(f"\n Top  {len(results)} similar cases: ")
#
#     for rank, r in enumerate(results, 1):
#         bar = "█" * int(r['similarity'] * 20)
#         print(f"\n {rank}  {r['name']} | "
#               f"\n Age  {r'age'}| "
#               f"\n Similarity: {r['similarity']:.2%} ")
#         print(f"     Symptoms : {', '.join(r['symptoms'])}")
#         print(f"     Diagnosis: {r['diagnosis']}")
#         print(f"     Match    : [{bar:<20}]")
#     print("=" * 55)
#
#
# # Base de données patients historiques
# patient_db = [
#     {"name": "Case_001", "age": 45,
#      "symptoms": ["chest pain", "difficulty breathing"],
#      "diagnosis": "Angina — referred to Cardiologist"},
#     {"name": "Case_002", "age": 32,
#      "symptoms": ["fever", "cough", "fatigue"],
#      "diagnosis": "Flu — prescribed rest and medication"},
#     {"name": "Case_003", "age": 67,
#      "symptoms": ["chest pain", "confusion", "dizziness"],
#      "diagnosis": "TIA — emergency neurology"},
#     {"name": "Case_004", "age": 28,
#      "symptoms": ["headache", "nausea", "dizziness"],
#      "diagnosis": "Migraine — prescribed triptans"},
#     {"name": "Case_005", "age": 55,
#      "symptoms": ["difficulty breathing", "fatigue", "cough"],
#      "diagnosis": "COPD exacerbation — pulmonology"},
# ]
#
# # Nouveau patient
# new_patient_symptoms = ["chest pain", "difficulty breathing","fatigue"]
# results = find_similar_patients(
#     new_patient_symptoms, patient_db, top_k=3
# )
# display_similarity_report(new_patient_symptoms, results)
#


# =======================================================#   VERSION 3   #=======================================================#

"""

"""

SYMPTOMPS_VOCABULARY = {
    "fever": 0,
    "cough": 1,
    "chest pain": 2,
    "difficulty breathing": 3,
    "headache": 4,
    "fatigue": 5,
    "nausea": 6,
    "dizziness": 7,
    "confusion": 8,
    "abdominal pain": 9,
}

import numpy as np

SYMPTOMPS_VOCABULARY_size = len(SYMPTOMPS_VOCABULARY)


def encode_symptoms(symptoms: list[str]) -> np.ndarray:
    vector = np.zeros(SYMPTOMPS_VOCABULARY_size, dtype=np.float32)

    for symptom in symptoms:
        idx = SYMPTOMPS_VOCABULARY.get(
            symptom.lower().strip())  # 1- on se place dans la liste. 2- On va dans la variable globale SYMPTOMPS_VOCABULARY et avec get on recupere l'index du symptom par tour de boucle
        if idx is not None:
            vector[idx] = 1.0
        else:
            vector[idx] = 1.0

    return vector


def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    norm1 = np.linalg.norm(
        v1)  # on recupere les distances des deux vecteurs exemple le v1 peut etre  : v1 = ['fievre', 'toux', 'dizzines'] en array on a: => v1 = np.array(v1) puis on encode : v1 = encode_symptoms(v1) et on recupere la taille : print(len(v1))=10
    norm2 = np.linalg.norm(v2)
    if norm1 == 0 or norm2 == 0:
        similarity = 0.0
        return similarity
    else:
        similarity = float(np.dot(v1, v2) / (norm1 * norm2))
        return similarity
    return similarity


def find_similarity_patients(query_symptoms: list[str], patient_database: list[dict], top_k: int = 3) -> list[dict]:
    similaryties = []
    query_vector = encode_symptoms(query_symptoms)
    for patient in patient_database:
        patient_vector = encode_symptoms(patient['symptoms'])
        similarity = cosine_similarity(query_vector, patient_vector)
        similaryties.append({**patient, "similarity": round(similarity, 4)})

    return sorted(
        similaryties, key=lambda x: x['similarity'], reverse=True
    )[:top_k]


def display_similarity_report(query: list[str], results: list[dict]) -> None:
    print(f"\n{'=' * 55}")
    print(f"{'MEDIROUTE AI — SIMILARITY SEARCH':^55}")
    print("=" * 55)

    print(f"\n   {','.join(query)}")
    print(f"\n Top {len(results)} similar cases.")
    print(f"  {'─' * 50}")

    for rank, r in enumerate(results, 1):
        bar = "█" * int(r[
                            'similarity'] * 20)  # affiche la barre x int(la valeur de la clee similaraity) x 20. DOnc plus similarity est grand plus il ya de barr █ . et comme c'est la boucle, on le fait pour tout.
        print(f"\n  #{rank} {r['name']} | "
              f"Age: {r['age']} | "
              f"Similarity: {r['similarity']:.2%}")
        print(f"     Symptoms : {', '.join(r['symptoms'])}")
        print(f"     Diagnosis: {r['diagnosis']}")
        print(f"     Match    : [{bar:<20}]")  # pas compris
        print("=" * 55)


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
new_patient_symptoms = ["chest pain", "difficulty breathing",
                        "fatigue"]
results = find_similarity_patients(new_patient_symptoms, patient_db, top_k=3)
display_similarity_report(new_patient_symptoms, results)











