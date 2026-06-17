import os
from openai import OpenAI

# 1. Fetch environment variables defined for the Agent from Agent Manager Deployment Configuration
openai_key = os.environ.get("OPENAI_API_KEY", "default key")

# 2. Show deployment variables
print(f" variable set : OpenAI Key : {openai_key}")


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
