# toujours utiliser with - fermeture garantie

#Ecrire -> toujours utiliser with
with open("patients.txt",   'w',   encoding='utf-8') as file:
    file.write("Patient: John | Age: 34 | Symptoms:fever\n")
    file.write("Patient: Sara | Age: 28 | Symptoms:cough\n")

#Lire Tout -> toujours utiliser with

with open("patients.txt",   "r",   encoding='utf-8') as file:
    content = file.read()
    print(content)

# Lire ligne par ligne - efficace pour gros fichiers -> toujours utiliser with

with open("patients.txt",   "r" , encoding = "utf-8") as file:
    for line in file:
        print(line)
        print(line.strip())

# Ajouter sans ecraser -> toujour avec with
with open ("patients.txt",  "a",    encoding='utf-8') as file:
    file.write("Patient: Bob | Age: 45 | Symptoms:headache\n")

#JSON - format standart pour configs et APIs

import json
config  = {"model":"gpt-4o",  "temperature":0.7}

# Sauvegarder grace a dump

with open ("configs.json",  "w",  encoding='utf-8') as file:
    json.dump(config, file, indent=4) #Dump est utiliser pour sauvegarder et charger les fichiers

# Charger
with open ("configs.json",  "r",  encoding='utf-8') as file:
    config = json.load(file)  #Dump est utiliser pour et charger pour la lecture des fichiers d'ou le 'r'



# A FAIRE : saugader les fichiers dans une dossier