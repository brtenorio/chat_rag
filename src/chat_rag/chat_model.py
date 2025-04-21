import getpass
import os
from langchain.chat_models import init_chat_model


class LLMmodel:
    def __init__(self, model="Haiku", max_num_tokens="256"):
        self.model = model
        self.max_num_tokens = max_num_tokens

    def load(self):
        if self.model == "Haiku":
            model_name = "claude-3-5-haiku-20241022"
        elif self.model == "Sonet":
            model_name = "claude-3-7-sonnet-20250219"
        llm = init_chat_model(
            model_name,
            model_provider="anthropic",
            configurable_fields="any",
            max_tokens=int(self.max_num_tokens),
            temperature=0.5,
            max_retries=2,
        )
        return llm
