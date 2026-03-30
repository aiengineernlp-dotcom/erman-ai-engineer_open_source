# comparateur_outils.py

def get_tool_recommandation(task: str) -> str:
    """
    Return a rigth tool for a given task
    Entreprise use Case: Onboarding tool for a new data scientist// tableau de bord pour savoir quel outils utiliser
    """
    recommendations = {
        'exploration': 'Jupiter NoteBook',
        'production':'Script.py',
        'presentation':'Google Colab',
        'deep_learning':'Google Colab (GPU)',
        'collaboration':'Google Colab',
        'versioning':'Script.py + Git'
    }

    return recommendations.get(task.lower(),"Task not recognized. Choose: exploration, production, presentation")

# Test du recommandeur

tasks = ['Exploration', 'production', 'presentation', 'deep_learning', '....okroejv', 'ppp']

print(f"    OUTILS RECOMMENDER PAR TACHES:")
print("=" * 140)
for task in tasks:
    tool = get_tool_recommandation(task)
    print(f"    -> Pour: {task:<20} -> Choisir: {tool}")