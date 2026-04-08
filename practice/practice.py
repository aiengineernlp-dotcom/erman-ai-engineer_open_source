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