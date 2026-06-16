import os
from openai import OpenAI

# Initialize the client. 
# It automatically picks up the 'OPENAI_API_KEY' environment variable.
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def generate_text(prompt: str) -> str:
    """A wrapper function inside your custom module."""
    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )
    return response.output_text
