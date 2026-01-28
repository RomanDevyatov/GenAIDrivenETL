import os
import requests


class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("LLM_API_KEY")

    def generate(self, prompt: str) -> str:
        # Placeholder for real API
        # Replace with OpenAI/Bedrock later
        print("\n--- LLM PROMPT ---\n", prompt)

        return "/* LLM output placeholder — replace with API call */"
