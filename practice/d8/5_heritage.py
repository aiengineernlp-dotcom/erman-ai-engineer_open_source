# 🚩🚩cette ligne🚩🚩d'ou vient-il? il fait quoi? pourquoi? il va ou? et cause/entraine quoi?#Classe  de base - interface commune

class BaseAssessment:
    """Base class for all Medical assessments"""

    def __init__(self, name: str) -> str:
        self.name = name

    def analyse(self, symptoms: list[str]) -> dict:
        """Must be implemented by subcalsses."""
        raise NotImplementedError(
            f"{self.name} must implement analyze()"
        )

    def format_report(self, result: dict) -> str:
        """Share method - avaible to all subclasses."""
        return (
                f"\n[{self.name.upper()} REPORT]\n" + "\n".join(f" {k}:{v}" for k, v in result.items())
        )


# Sous-classe - specialise le comportement

class UrgencyClassifier(BaseAssessment):
    """Classifies urgency level from symptoms."""

    URGENT_SYMPTOMS = {
        "chest pain", "difficulty breathing",
        "unconscious", "severe bleeding", "stroke"
    }

    MODERATE_SYMPTOMS = {
        "high fever", "severe headache",
        "persistent vomiting", "confusion"
    }

    def __init__(self):
        # 🚩🚩cette ligne🚩🚩d'ou vient-il? il fait quoi? pourquoi? il va ou?
        super().__init__("Urgency Classifier")

    def analyse(self, symptoms: list[str]) -> dict:
        symptoms_lower = [s.lower() for s in symptoms]

        if any(s in self.URGENT_SYMPTOMS for s in symptoms_lower):
            level = "EMERGENCY"
            action = "Go to ER immediately"
        elif any(s in self.MODERATE_SYMPTOMS for s in symptoms_lower):
            level = "MODERATE"
            action = "see doctor within 24h"
        else:
            level = "LOW"
            action = "Schedule appointment"
        return {
            "urgency": level,
            "action": action,
            "symptoms_counts": len(symptoms)
        }


class SpecialistRouter(BaseAssessment):
    """Routes patients to the rigth specialist."""

    ROUTING = {
        "heart": "Cardiologist",
        "chest": "Cardiologist",
        "skin": "Dermatologist",
        "breathing": "Pulmonologist",
        "headache": "Neurologist",
        "fever": "General Practitioner",
        "stomach": "Gastroenterologist",
    }

    def __init__(self):
        # 🚩🚩cette ligne🚩🚩d'ou vient-il? il fait quoi? pourquoi? il va ou? et cause/entraine quoi?
        super().__init__("Specialist Router")

    def analyse(self, symptomes: list[str]) -> dict:
        # 🚩🚩cette ligne🚩🚩d'ou vient-il? il fait quoi? pourquoi? il va ou? et cause/entraine quoi?
        specialistes = set()
        for symptom in symptomes:
            for keyword, specialist in self.ROUTING.items():
                if keyword in symptom.lower():
                    specialistes.add(specialist)
        return {
            "recommanded_specialists": list(specialistes) or ["General Practitioner"],
            "symptoms_analysed": symptoms
        }


# polymorphisme -> meme interface, comportements differents

assessments = [UrgencyClassifier(), SpecialistRouter()]

symptoms = ["chest pain", "difficulty breathing"]

for assessment in assessments:
    result = assessment.analyse(symptoms)
    print(assessment.format_report(result))
