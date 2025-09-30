from litellm import completion

class BedrockLLM:
    def __init__(self, model="bedrock/amazon.titan-text-lite-v1", temperature=0.7, max_tokens=512):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate(self, prompt: str) -> str:
        response = completion(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        return response["choices"][0]["message"]["content"]
