def calculate_token_cost(prompt_tokens: int, completion_tokens: int, model: str = "gpt-4o",
                         currency: str = "USD") -> dict:
    """
    Calcule le token cost d'un appelle lorsque le client (moi) passe une commande au LLM via son l'API d'un fournisseur.
    Args:
        - prompt_tokens: le nombre de mots que j'envoie au model (llm(claude ou chat gpt 4o)) du fournisseur ,
        - completion_tokens: le nombre de mots que je reçois apres traitement,
        - model :  default gpt-4o,
        - currency: defaut usd,
    Returns:
        - dict :
    Raises:

        - ValueError

    """

    pricing = {
        "gpt-4o": {"input": 0.0025, "output": 0.010},
        "gpt-4o-mini": {"input": 0.00015, "output": 0.0006},
        "claude-sonnet": {"input": 0.003, "output": 0.015},
    }

    if not model in pricing:
        raise ValueError(
            f"Model {model} is not supported",
            f"Choose from : {list(pricing.keys())}"
        )
    rates = pricing[model]

    input_cost = (prompt_tokens / 1000) * rates["input"]
    output_cost = (completion_tokens / 1000) * rates["output"]
    total_cost = input_cost + output_cost

    return {
        "model": model,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "input_cost": round(input_cost, 4),
        "output_cost": round(output_cost, 4),
        "total_cost": total_cost,
        "currency": currency
    }


cost = calculate_token_cost(prompt_tokens=1500, completion_tokens=300, model="gpt-4o")
print(f"Total: ${cost['total_cost']:.6f}")




