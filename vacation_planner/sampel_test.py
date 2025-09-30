
from litellm import completion

response = completion(
    model="bedrock/amazon.titan-text-lite-v1",
    messages=[{"role": "user", "content": "Hello, how are you?"}],
    temperature=0.7,
    max_tokens=512
)

print(response["choices"][0]["message"]["content"])
