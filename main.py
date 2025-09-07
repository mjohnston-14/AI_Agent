import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def main():
    #print(f"{len(sys.argv)}")
    if len(sys.argv) < 2:
        print("Error: No input prompt, aborting...")
        exit(1)
    else:
        print(f"Hello from ai-agent!\nSent Query of: {sys.argv[1]} ")
    response = client.models.generate_content(model='gemini-2.0-flash-001',contents=f"{sys.argv[1]}")
    print(response.text)
    #print(response.usage_metadata)
    #print(response.usage_metadata.prompt_token_count)
    #print(response.usage_metadata.candidates_token_count)

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
