import ollama

MODEL = "llama3.2:1b"


def ask(prompt, system="You are a careful AI assistant."):
    """Send a prompt to the local language model."""
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
    )

    return response.message.content.strip()