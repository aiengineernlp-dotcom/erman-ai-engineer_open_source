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


def mock_api_call(prompt: str, model: str, fail_rate: float = 0.4) -> dict:  # fonction qui va simuler un appel API
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

        "content": f"[Mock response to {prompt[:40]}...]",  # dans le prompt on prend les premiers 40 caracteres

        "usage": {
            "prompt_tokens": len(prompt.split()),  # prompt entre
            "completion_tokens": 50,  # nombre de prompt de sorti
            "total_tokens": len(prompt.split()) + 50  # la somme prompt entrer + prompt
        }
    }


def call_with_retry(
        prompt: str,
        model: str = "gpt-4o",
        max_retries: int = 3,
        base_delay: float = 1.0,
        fallback_model: str = "gpt-4o-mini"
) -> dict:
    """

    Call LLM API with exponential backoff retry.

    Strategy:
         - RatelimitError -> wait then retry
         - APITimeOutError -> retry immediatly (up to max)
         - InvalidRequestError -> fail fast (no retry)
         - All retries exhausted -> try Fallback model
    """

    last_error = None

    for attempt in range(1, max_retries + 1):
        current_model = model if attempt <= max_retries else fallback_model

        try:
            with llm_call_timer(current_model):  # on appelle la fonction ->>>>> llm_call_timer()
                result = mock_api_call(prompt, current_model)  # on appelle la fonction ->>>>> mock_api_call ()
            return {
                **result,
                "attempts": attempt,
                "final_model": current_model
            }
        except InvalidRequestError as e:
            # non recuperable - arret immediat
            raise RuntimeError(
                f"Invalid request (no retry): {e}"
            ) from e

        except RatelimitError as e:
            wait = min(base_delay * (2 ** attempt), 30)
            print(f" ⏳ Rate limited. waiting {wait:.1f}s"
                  f"(attempt {attempt}/{max_retries})")
            time.sleep(wait)
            last_error = e

        except (APITimeOutError, LLMError) as e:
            if attempt < max_retries:
                wait = base_delay * attempt
                print(f" 🔄 Retriying in {wait:.1f}s"
                      f"(attempt {attempt}/{max_retries})")
                time.sleep(wait)
            last_error = e

    # Fallback model
    print(f"\n ⚠️ ")











