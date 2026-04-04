# encapsulation : protection des donnees (variables)

class MedicalRecord:
    """
    Encapsulate(proteger) sensitive patients data.
    Private attributes = not accessible directly.
    """

    def __init__(self,patient_id: str, diagnosics : str) -> str:
        self._patient_id = patient_id # proteger - par convention (1 underscore)
        self.__diagnosics = diagnosics  # privé - name mangling (2 underscores)

    #Getter - acces controlé
    @property
    def diagnosics(self) -> str:
        return self.__diagnosics

    # Setter - validation avant modification
    @diagnosics.setter
    def diagnosics(self, value : str) -> None:
        if not value.strip(): # si on ne peut pas faire "value.strip()" ca veux dire que il ya pas le texte d'ou le raise
            raise ValueError("Diagnosics can not be empty")
        self.__diagnosics = value.strip().lower() # nottoyage du texte pour retirer les espaces indesirables et le mettre en minuscule

record = MedicalRecord("P001","Hypertension")
print(record._patient_id)
print(record.diagnosics) # -> Hypertension
record.diagnosics = "Diabetes" # passe par le setter
print(record.diagnosics)




