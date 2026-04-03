


"""
Imagine le fournisseur comme un restaurant:


Le Client (Toi) -> Tu passes commande via l'API(le serveur).
Le LLM (Le Chef)-> Il est en cuisine. Il reçoit ta commande, réfléchit, et prépare le plat (la réponse).
Le Fournisseur (Le Patron du resto) -> Il ne cuisine pas, mais il surveille tout.

Il compte combien d'ingrédients tu as demandés (Tokens d'entrée) et combien de grammes de nourriture le chef a cuisinés
(Tokens de sortie).

La Réponse -> Le serveur (API) t'apporte ton plat.

La Facture -> Le patron n'attend pas que le chef lui fasse un rapport ; ses capteurs ont déjà tout enregistré
automatiquement au moment où les données ont traversé ses serveurs.
Ce qui est inscrit sur ta facture :Le fournisseur enregistre deux compteurs pour chaque appel :

Prompt Tokens -> Ce que tu as envoyé.

Completion Tokens -> Ce que le LLM a généré.

C'est l'addition de ces deux mesures, multipliée par le prix de ton modèle (ex: Claude 3.5 Sonnet), qui donne ton coût
total.

"""

# see this code : practice/calculate_token_cost.py