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

    context = []

    while True:
        user_input = input("> ")

        if user_input == ":q":
            exit()

        context.append({
            "role": "user",
            "content": user_input,
        })

        resp = client.messages.create(
            model=model_name,
            max_tokens=2048,
            messages=context,
        )

        for block in resp.content:
            if block.type == "text":
                context.append({
                    "role": "assistant",
                    "content": block.text,
                })
                print(block.text)
