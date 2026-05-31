from groq import Groq
from dotenv import load_dotenv
import os

print("Starting program...")

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

print("API key loaded")

client = Groq(api_key=api_key)

print("Reading README.md...")

with open("README.md", "r", encoding="utf-8") as file:
    spec_text = file.read()

print("Specification loaded")
print("Calling Groq...")

prompt = f"""
You are a senior backend software architect.

Based on the specification generate:

## Section 1: Features Identified

List all features extracted from the specification.

## Section 2: API Specification Table

Columns:
- API Endpoint
- HTTP Method
- Purpose
- Request Body
- Response Body
- Authentication Required

## Section 3: Assumptions

List any assumptions made while generating the APIs.

Specification:
{spec_text}
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.2
)

print("Response received!\n")
print(response.choices[0].message.content)