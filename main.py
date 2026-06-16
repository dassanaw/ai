import os
from openai import OpenAI

# 1. Initialize the client (Reads OPENAI_API_KEY from environment variables)
client = OpenAI()

def run_chat_agent():
    print("🤖 Chat Agent Initialized! Type 'exit' or 'quit' to end the session.\n")
    
    # 2. Define system-level behaviors and initialize memory
    messages = [
        {"role": "system", "content": "You are a helpful, concise AI coding assistant."}
    ]
    
    while True:
        # 3. Capture user input
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
            
        # Append user message to conversation history
        messages.append({"role": "user", "content": user_input})
        
        try:
            # 4. Generate the streaming response from the model
            response = client.chat.completions.create(
                model="gpt-4o",  # Or your chosen model
                messages=messages,
                stream=True
            )
            
            print("Agent: ", end="", flush=True)
            assistant_response = ""
            
            for chunk in response:
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    print(content, end="", flush=True)
                    assistant_response += content
            print("\n")
            
            # Append assistant response to preserve conversation history
            messages.append({"role": "assistant", "content": assistant_response})
            
        except Exception as e:
            print(f"\n Error encountered: {e}\n")

if __name__ == "__main__":
    run_chat_agent()
