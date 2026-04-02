#llm_client_retry.py
"""
Production LLM Client with retry Logic.
Use case: Resilient LLM API calls with exponential backoff.
Pattern: Used in all Production AI systems.

Stack: Execption + Context managers -> foundations for LanChain clients
"""
import time
import random
from contextlib import contextmanager

class LLMError (Exception):
    """Base LLM Error."""
    pass

class RatelimitError(LLMError):
    def __init__(self, retry_after: int = 60):
        self.retry_after = retry_after
        super().__init__(f"Rate limit. Retry after {retry_after}s")

class APITimeoutError(LLMError):
    def __init__(self,timeout:int):
        super().__init__(f"API timeout after {timeout}s")

class InvalidRequestError(LLMError):
    """Non-recoverable - bad prompt pr params"""
    pass

class ModelNotAvaibleError(LLMError):
    """Model is down or deprecated"""
    pass

@contextmanager

def llm_call_timer(model:str):
    """Context manager to time and log LLM calls"""
    start = time.time()
    print(f"    > Calling {model}...")
    try:
        yield
        elapsed = time.time() - start
        print(f"    ✅ Success in {elapsed:.3f}s")
    except Exception as e:
        elapsed = time.time()  - start
        print(f"    ❌ Failed after {elapsed:.3f}s : {type(e).__name__}")
        raise


def mock_api_call(prompt: str, model:str,fail_rate:int) -> dict:
    """
    Simulate an LLM API call with random faillure.
    fail_rate: probalibity of faillure on each attempt.
    """

    time.sleep(0.05) # simulate a network latency

    rand = random.random()

    if rand < fail_rate *0.3:
        raise RatelimitError(retry_after=2)
    elif rand < fail_rate * 0.6:
        raise APITimeoutError(timeout = 30)
    elif rand<fail_rate:
        raise LLMError("internal Server error")

    # success
    return{
        "model" : model,
        "content":f"[Mock response to: {prompt[:40]}...]",
        "usage":{

            "prompt_tokens": len(prompt.split()),
            "completion_tokens":50,
            "total_tokens":len(prompt.split())+50
        }
    }


def call_with_retry():
    pass

def display_result():
    pass
