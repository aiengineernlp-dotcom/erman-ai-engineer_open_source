# CONCEPT DE CLASSE ET INSTANCE (object)

class Patient:
    """Represents a patient in MRAI."""
    total_patients = 0
    # ATTRIBUTS DE CLASSE - PARTAGER PAR TOUTES LES INSTANCES (objects)
    def __init__(self, name: str, age: int, symptoms: list[str], gender: str):
        #attribut d'instance propre a chaque patients
        self.name       = name
        self.age        = age
        self.symptoms   = symptoms
        self.gender     = gender
        self.id         = Patient.total_patients + 1
        Patient.total_patients = Patient.total_patients + 1

    def describe(self) -> str:
        """ Méthode d'Instance (object)  - qui va acceder aux attributs de l'instance (object) """
        return (
            f"Patient #{self.id} : {self.name}| "
            f"Age: {self.age} |"
            f"Symptoms: {', '.join(self.symptoms)} | "  # pour joindre les symptoms eviter l'affichage en forme de liste 🚩🚩
            f"Gender: {self.gender} |"
        )

    @classmethod  # methode qui est uniquement utiliser par la classe 🚩🚩
    def from_dict(cls, data: dict) -> "Patient":
        """Class method - crée un patient depuis un dictionnaire. donc il faut deja avoir un dictionnaire"""  # mais je me demande pourquoi faire quelque chose chose comme ca? le test? 
        return cls(
            name=data["name"],
            age=int(data["age"]),
            symptoms=data.get("symptoms", "").split(","),
            # pour le .get c'est juste une autre methode de recuperer les elements du dictionnaire. pour le split() faut revoir son use
            gender=data.get("gender")

        )

    @staticmethod
    def is_urgent(symptoms: list[str]) -> bool:
        """Static method - ne depend pas de l'instance (object)."""
        urgent = {"chest pain", "difficulty breathing", "unconscious", "severe bleeding"}

        return any(s.lower() in urgent for s in symptoms)  # comprend ici avec any() function 
        # for s in symptoms:  continue ici


# utilisation
p1 = Patient("John", 34, ["fever", "cough"], "male")
p2 = Patient("Sara", 28, ["chest", "pain"], "female")

print(p1.describe())
print(Patient.is_urgent(p2.symptoms))
print(Patient.total_patients)


# probleme rencontrer sur les variables de classes cas de
# total_patients = 0


