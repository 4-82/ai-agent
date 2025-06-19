import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    if ("-v" in sys.argv[1:]) or ("--verbose" in sys.argv[1:]):
        generate_content_verbose(client, messages)
    else:
        generate_content(client, messages)
    

def generate_content(client, messages):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print(f"Response:\n {response.text}")

def generate_content_verbose(client, messages):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print(f"Response:\n {response.text}\nUser prompt: {" ".join(sys.argv[1:])} Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()

