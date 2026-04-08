"""
Production LLM Client with Retry logic.
Cas d'utilisation: Resillient LLM API calls with exponential backoff.
Stack : Exceptions + Context managers

"""
import random
import time
from contextlib import contextmanager  # trouver son importance


# Exception personnalisees
class LLMError(Exception):
    """Base LLM error"""
    pass


class RateLimitError(LLMError):
    def __init__(self, retry_after: int = 60):
        self.retry_after = retry_after
        super().__init__(
            super().__init__(
                f"Rate limit. Retry after {retry_after}s")  # cette ligne est pour recuperer les elements venant de la classe "MERE -> LLMError" dans ce cas c'est juste le message.


class APITimeOutError(LLMError):
    def __init__(self, timeout: int):
        super().__init__(f"API Timeout after {timeout}s")


class InvalidRequestError(LLMError):
    def __init__(self):
        super().__init__(f"Non-recoverable - Bad prompt or params")
        pass


class ModelNotAvaibleError(LLMError):
    def __init__(self):
        # super().__init__(f"Model is down or deprecated")
        pass


# AUTRES CLASSES A CREER PLUS TARDS :
@contextmanager
def llm_call_timer(model: str):
    """ context manager to time and log LLM calls. """  # imagine la duree entre  l'heure du depart et celle d'arriver d'un avion. d = arrviver - depart
    start = time.time()
    print("f  > Calling {model}...")
    try:
        yield
        ecoule = time.time() - start  # calcul tu temps ecouler (durer) entre end et start
        print(f" ✅ Success in {ecoule:.3f}s")
    except Exception as e:
        ecoule = time.time() - start  # calcul tu temps ecouler (durer) entre end et start
        print(f"   ❌Failed after {ecoule:.3f}s: {type(e).__name__}")
        raise


def mock_api_call(prompt: str, model: str, fail_rate: float = 0.4) -> dict:
    """
    Simulate an LLM API call with randon faillures.
    fail_rate : probalilite of failure on each attempt
    """
    time.sleep(0.05)  # simulate network latency
    rand = random.random()
    if rand < fail_rate * 0.3:
        raise RateLimitError(retry_after=2)

    elif rand < fail_rate * 0.6:
        raise APITimeOutError(timeout=30)
    elif rand < fail_rate:
        raise LLMError("Internal server error")

    # success

    return {
        "model": model,
        "content": f"[Mock response to {prompt[:40]}...]",
        "usage": {
            "prompt_tokens": len(prompt.split()),  # entre utilisateur
            "completion_tokens": 50,  # la reponse du llm
            "total_tokens": len(prompt.split()) + 50
        }
    }


def call_with_retry(prompt: str, model: str = "gpt-4o", base_delay: float = 1.0, max_retries: int = 3,
                    fallback_model: str = "gpt-4o-mini") -> dict:
    """
    Call LLM API with exponential backoff retry.

    strategy:
        - RateLimitError -> wait then retry
        - APITimeOutError -> retry immediately (up to max)
        - InvalidRequestError -> Fail fast (no retry)
        - All retries exhausted -> try fallback model
    """

    last_error = None

    for attempt in range(1, max_retries + 1):
        current_model = model if attempt <= max_retries else fallback_model

        try:
            with llm_call_timer(current_model):
                result = mock_api_call(prompt, current_model)
            return {**result,
                    "attempts": attempt,
                    "final_model": current_model
                    }

        except InvalidRequestError as e:
            # Non - recuperable - arrêt immédiat
            raise RuntimeError(
                f"Invalite request (no retry) : {e}"
            ) from e

        except RateLimitError as e:
            wait = min(base_delay * (2 ** attempt), 30)
            print(f" ⏳ Rate limited. waiting {wait:.1f}s"
                  f"   (attempt {attempt}/{max_retries})")

            time.sleep(wait)
            last_error = e

        except (APITimeOutError, LLMError) as e:
            if attempt < max_retries:
                wait = base_delay * attempt
                print(f"🔄 Retriying in {wait:.1f}s"
                      f"    (attempt {attempt}/{max_retries})")
                time.sleep(wait)

                last_error = e

    # FALLback model
    print(f"\n    ⚠️ Switching to fallback model: {fallback_model}")
    try:
        with  llm_call_timer(fallback_model):
            result = mock_api_call(prompt, fallback_model, fail_rate=0.1)
        return {

            **result,
            "attempts": max_retries + 1,
            "final_model": fallback_model,
            "used_fallback": True
        }
    except Exception as e:
        raise RateLimitError(
            f"All retries and fallback failed. Last error: {last_error}"
        ) from e

def display_results(result: dict) -> None:
    print(f"\n {'=' * 50}")
    print(f"{'LLM CALL RESULT': ^50}")
    print('=' * 50)
    print(f"    Model  :   {result.get('final_model', 'unknown')}")
    print(f"    Attempt :   {result.get('attempts', '?')}")
    print(f"    Fallback used : {result.get('used_fallback', False)}")
    print(f"    Total tokens  : {result['usage']['total_tokens']}")
    print(f"    Content       : {result['content']}")
    print(f"=" * 50)


# test
random.seed(42)

prompts = [
    "What is retrieval augmented generation?",
    "Explain vector database in simple terms",
    "How does LangChain works? ",
    "comment tu t'appelles?"
]

for prompt in prompts:
    print(f"\n {'-' * 50}")
    print(f"Prompt: {prompt}")
    try:
        result = call_with_retry(prompt, max_retries=3)
        display_results(result)
    except RuntimeError as e:
        print(f"   ❌ FATAL: {e}")













