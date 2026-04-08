import time
from contextlib import contextmanager
import random


class LLMError(Exception):
    """Base Message Error"""
    pass


class RatelimitError(LLMError):
    def __init__(self, retry_after: int = 60):
        self.retry_after = retry_after
        super().__init__(f"Rate limit Error. Retry after {retry_after}s")


class APITimeOutError(LLMError):
    def __init__(self, timeout: int):
        self.timeout = timeout
        super().__init__(f"API timeout after {timeout}s")


class InvalidRequestError(LLMError):
    def __init__(self, attribut):
        self.attribut = attribut
        super().__init__(f" Invalid Request - bad prompt or bad params ")
        pass


class ModelNotAvaibleError(LLMError):
    def __init__(self, attribut):
        self.attribut = attribut
        super().__init__(f"message")
        pass


@contextmanager
def llm_call_timer(model: str):
    """ Context manager to time and log LLM calls.  """
    start = time.time()  # capture du temps actuel dans la variable start
    print(f" >> Calling model {model} ...")
    try:
        yield
        ecouler_time = time.time() - start
        print(f"    ✅ Success in {ecouler_time:.3f}s")
    except Exception as e:
        ecouler_time = time.time() - start
        print(f"   ❌ Echec au bout de  {ecouler_time:.3f}s : {type(e).__name__}")


def mock_api_call(prompt: str, model: str, fail_rate: float = 0.4) -> dict:
    """Simulate an LLM API call with random failures.
    fail_rate: probaility of failure on each attempt.
    """
    time.sleep(
        0.05)  # simulate the network latency / reccreer un delai artifiellement que mettra l'appel/ fait patienter le programme

    rand = random.random()  # genere un nombre entre 0 et 1

    """LOGIQUE: 
    -> A l'appelle de la fonction:
    "Attends d'abord un peu (0.05s), puis tire au sort (rand) pour voir si, après cette attente, le serveur nous répond normalement ou 
    nous envoie une erreur (basée sur le fail_rate)."Sans le time.sleep, l'erreur arriverait en 0,0001 seconde, ce qui ne permettrait 
    pas de tester si l' application reste fluide pendant que le réseau "travaille".   """

    if rand < fail_rate * 0.3:
        raise RatelimitError(retry_after=2)  # reprend apres 2 secondes
    elif rand < fail_rate * 0.6:
        raise APITimeOutError(timeout=30)
    elif rand < fail_rate:
        raise LLMError("Internal server Error")

    # Succes

    return {
        "model": model,

        "content": f"[Mock response to {prompt[:40]}...]",

        "usage": {
            "prompt_tokens": len(prompt.split()),
            "completion_tokens": 50,
            "total_tokens": len(prompt.split()) + 50
        }
    }






