#================VERSION 1


"""LLM  output PARSER(analyse/traite/extrait) using Regex.
Use case : Extraire des données structurées à partir de réponses non structurées d'un LLM"
           (Modèle Linguistique étendu comme GPT-4, Claude, Gemini, etc.)

"""
import re
import json
from typing import Optional

class LLMOutputParser:
    """
    PARSER(analyse/traite/extrait) differents output into structured python objects like JSON, lists and so on ..
    Handles: JSON blocks, key-values paires (dictionnaires), lists , scores.
    """



    PATTERNS = {
        "json_block" : re.compile(r' ```(?:json)?\s*(\{.*?\}|\[.*?\]\s*)```', re.DOTALL),
        "json_inline" : re.compile(r'(\{[^{}]+\})', re.DOTALL),
        "score" : re.compile (r'(?:score|rating|confidence)[:\s]+([0-9.]+)',re.IGNORECASE),
        "percentage": re.compile(r'([0-9.]+)\s*%'),
        "key_value" : re.compile(r'^([A-Za-z][A-Za-z0-9_\s]*?:\s*(.+)$)',re.MULTILINE),
        "bullet_list": re.compile(r'^[-*•]\s*(.+)$',re.MULTILINE),
        "numbered_list": re.compile(r'^\d+[.)]\s*(.+)$',re.MULTILINE),
        "emails":re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
        "urls":re.compile(r'https?://[^\s<>"{}|\\^`\[\]]+'),
    
    }


def extract_json(self, text:str)-> Optional[dict | list]:
    """Extract First valide Json from LLM Output. """
    # essaye d'abors les blocs de code markdown 

    match = self.PATTERNS['json_block'].search(text)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecoderError:
            pass

    # Essay le Json inline 

    for match in self.PATTERNS["json_inline"].finditer(text):
        try:
            return json.loads(match.group(1))

        except json.JSONDecoderError:
            continue
    raise ValueError("No Valid JSON found in the output LLM")


def extract_score(self, text:str)-> Optional [float]:
    """Extract numerical score form LLM Output"""

    # chercher score explicite

    match = self.PATTERNS["score"].search(text)

    if match :
        try:
            return float(match.group(1))
        except ValueError:
            pass

    # chercher pourcentage

    match = self.PATTERNS["percentage"].search(text)

    if match :
        try:
            return float(match.group(1))/100
        except ValueError:
            pass
    return None     # pourquoi 


def extract_key_values(self,text:str)->dict:
    """Extract key values paire from structured LLM output"""

    matches = self.PATTERNS["key_value"].findall(text)

    return {
        key.strip(): value.strip() for key,value in matches
    }



    


    
    