LLM  output PARSER(analyse/traite/extrait) using Regex

"""
## Définition du concept
"Unstructured LLM Outputs" (Sorties non structurées) : L'IA génère une réponse textuelle "naturelle" (ex: un long paragraphe) qui est facile à lire pour un humain, mais difficile à traiter automatiquement par un logiciel.
Exemple : "L'utilisateur s'appelle Jean Dupont, il habite 10 rue de Paris, et son numéro est le 0601020304."
"Extract Structured Data" (Extraire des données structurées) : Le processus de forcer l'IA à extraire des informations précises et à les placer dans un format standardisé comme le JSON.
Exemple (JSON) : {"nom": "Jean Dupont", "adresse": "10 rue de Paris", "tel": "0601020304"}


## "Use Case" (Cas d'usage) : Scénarios concrets où cette technique est appliquée.
#Exemples Concrets de cette Utilité 
Traitement de documents : Transformer des factures PDF ou des contrats scannés en données exploitables.
Analyse de retours clients : Analyser des avis ou des emails de support pour extraire le sentiment, le produit concerné et le problème cité.
Extraction d'entités : Tirer des noms de personnes, des lieux ou des montants financiers d'un article de presse.


## Pourquoi faire cela ? (Avantages)
Automatisation : Évite la saisie manuelle de données.
Fiabilité : Les LLMs modernes (via "function calling" ou bibliothèques comme Instructor) peuvent garantir le formatage des données.
Intégration : Permet de stocker les informations dans des bases de données SQL ou NoSQL pour des analyses ultérieures. 


SEE: practice/llm_output_parser.py 

