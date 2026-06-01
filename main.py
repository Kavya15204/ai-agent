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

spec_file = input("Enter spec file path: ")

with open(spec_file, "r", encoding="utf-8") as file:
    spec_text = file.read()

print("Specification loaded")

# =========================
# API GENERATION
# =========================

print("Generating API Specification...")

api_prompt = f"""
You are a backend software architect.

Generate a detailed API specification table.

Include:
- API Endpoint
- HTTP Method
- Purpose
- Request Body
- Response Body
- Authentication Required

Return in markdown table format.

Specification:
{spec_text}
"""

api_response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": api_prompt}
    ],
    temperature=0.2
)

api_output = api_response.choices[0].message.content

print("\n===== API SPECIFICATION =====\n")
print(api_output)

# =========================
# HLD GENERATION
# =========================

print("\nGenerating High Level Design...")

hld_prompt = f"""
You are a Principal Software Architect.

Read the specification and create a PROFESSIONAL High Level Design document.

Include:

1. Executive Summary
2. Functional Requirements
3. Assumptions
4. Recommended Technology Stack
   - Frontend
   - Backend
   - Database
   - Authentication
   - Hosting / Cloud
5. System Components
6. High Level Architecture Flow
7. Component Interaction Flow
8. Database Design
9. Security Design
10. Scalability Considerations
11. Reliability Considerations
12. Monitoring and Logging
13. Future Enhancements
14. Mermaid Architecture Diagram

Specification:
{spec_text}
"""

hld_response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": hld_prompt}
    ],
    temperature=0.2
)

hld_output = hld_response.choices[0].message.content

print("\n===== HIGH LEVEL DESIGN =====\n")
print(hld_output)