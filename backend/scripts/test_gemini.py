import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("AQ.Ab8RN6K1vi3hpWruiSrPjj6OgQ1uW_7FvlOIUegScptb3JzJGQs")

client = genai.Client(api_key=api_key)

sentence = "I am very excited about building my new project."

response_format = {
    "type": "text",
    "mime_type": "application/json",
    "schema": {
        "type": "object",
        "properties": {
            "sentiment": {
                "type": "string"
            },
            "word_count": {
                "type": "integer"
            }
        },
        "required": ["sentiment", "word_count"]
    }
}

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=f"Analyze this sentence: {sentence}",
    response_format=response_format
)

result = json.loads(interaction.output_text)

print(result)
print(type(result))