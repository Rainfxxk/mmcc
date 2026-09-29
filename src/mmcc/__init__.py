import os
from anthropic import Anthropic


api_key = os.getenv('MINI_MINI_CLAUDE_API_KEY')
base_url = os.getenv('MINI_MINI_CLAUDE_BASE_URL')
model_name = os.getenv('MINI_MINI_CLAUDE_MODEL_NAME')


def main() -> None:

    client = Anthropic(
        api_key=api_key,
        base_url=base_url,
        timeout=600,
    )
    while True:
        user_input = input("> ")
        resp = client.messages.create(
            model=model_name,
            max_tokens=2048,
            messages=[{
                "role": "user",
                "content": user_input
            }],
        )
        for block in resp.content:
            if block.type == "text":
                print(block.text)
