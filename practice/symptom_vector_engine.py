# les embedings des symptoms sont la base de MEDIROUTE AI. car il est utiliser pour comparer les symptoms

import numpy as np

# dictionnaire de symptomes -> indices

SYMPTOME_VOCABULARY = {
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
N_SYMPTOMES = len(SYMPTOME_VOCABULARY)


def encode_symptoms(symptoms: list[str]) -> np.ndarray:
    """
    Encode une liste de string comme un vecteur binaire
    1= symptom present
    0= symptom absent.
    """
    vector = np.zeros(N_SYMPTOMES, dtype=np.float32)  #

    for symptom in symptoms:
        idx = SYMPTOME_VOCABULARY.get(symptom.lower())
        if idx is not None:
            vector[idx] = 1.0
    return vector


def cosine_similarity(v1: np.ndarray,
                      v2: np.ndarray) -> float:
    """
    Compute cosine similarity between two vectors.
    Range: [0, 1] - 1 = identical, 0 = completly different.
    """

    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return float(np.dot(v1, v2) / (norm1 * norm2))


def find_similar_patients(
        query_symptomps: list[str],
        patient_database: list[dict],
        top_k: int = 3
) -> list[dict]:
    """
    Regarde le patient le plus similaire dans la base de donnees
    Args:
        - query_symptomps: symptoms du nouveau patients
        - patient_database: donnees historiques des patients
        - top_k : number of similar cases to return
    """

    query_vector = encode_symptoms(query_symptomps)

    similarities = []
    for patient in patient_database:
        patient_vector = encode_symptoms(patient["symptoms"])
        similarity = cosine_similarity(query_vector, patient_vector)
        similarities.append({**patient, "similarity": round(similarity, 4)})

    return sorted(
        similarities,
        key=lambda x: x["similarity"],
        reverse=True
    )[:top_k]

def display_similarity_report(query: list[str], results: list[dict]) -> None:
    print(f"\n {'=' * 55} ")
    print(f"{'MEDIROUTE AI SIMILARITY SEARCH':^55}")
    print(f"=" * 55)
    print(f"    Query symptoms : {', '.join(query)}")  ##
    print(f"\n  Top {len(results)} similar cases:")
    print(f"    {'-' * 55}")

    for rank, r in enumerate(results, 1):
        bar = '❚' * int(r["similarity"] * 20)

        print (f"\n    #{rank} {r['name']}|"
               f"\n    Age: {r['age']}| "
               f"\n    Similarity: {r['similarity']:.2%}")

        print(f"\n     Symptoms : {', '.join(r['symptoms'])}")
        print(f"\n     Diasgnostic: {r['diagnosis']}")
        print(f"\n     Match :[{bar:<20}]")
        print(f"=" * 55)
# base de donnnees des patients (historiques)

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
# nouveau patient

new_patient_symptoms = ["chest pain", "difficulty breathing", "fatigue"]

results = find_similar_patients(
new_patient_symptoms,
patient_db,
top_k = 3)

display_s_report = display_similarity_report(new_patient_symptoms, results)

print(new_patient_symptoms)
print(display_similarity_report)







