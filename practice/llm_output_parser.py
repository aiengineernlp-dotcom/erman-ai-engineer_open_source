"""
LLM  output PARSER(analyse/traite/extrait) using Regex.
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

    # patterns compilés performaces sur de gros volumes de donnees

    PATTERNS = {
        "json_block": re.compile(r'```(?:json)?\s*(\{.*?\}|\[.*?\])\s*```', re.DOTALL),

        "json_inline": re.compile(r' (\{[^{}]+\})', re.DOTALL),

        "score": re.compile(r'(?:score|rating|confidence)[:\s]+([0-9.]+)'), re.IGNORECASE),

        "percentage": re.compile(r'([0-9.]+)\s*%'),

        "key_value": re.compile(r'^([A-Za-z_][A-Za-z0-9_\s]*?):\s*(.+)$'), re.MULTILINE),

        "bullet_list": re.compile(r'^[-*•]\s* (.+)$', re.MULTILINE),

        "numbered_list": re.compile(r'^\d+[.)\s]*(.+)$'), re.MULTILINE),

        "emails": re.compile(r'\b[A-Za-z0-9._%+-]@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}b'),

        "urls": re.compile(r'https?://[^s<>"{}|\\^`\[\]]+'),

    }

