
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# Load .env from the project root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Check API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY is missing. Check your root .env file."
    )

client = Groq(api_key=api_key)

SYSTEM_PROMPT = """
You are a professional AI chatbot for a digital marketing company.

Answer questions related to:
- SEO
- Social Media Marketing
- Google Ads and PPC
- Content Marketing
- Email Marketing
- Affiliate Marketing
- Website Marketing
- Lead Generation
- Branding
- Digital Advertising
- Analytics
- Conversion Rate Optimization

Answer clearly, accurately, and helpfully.
If a question is unrelated to digital marketing, politely
explain your specialization and redirect the user.
Do not invent company-specific information.
Keep answers concise unless more detail is requested.
"""

def get_response(user_message: str) -> str:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        temperature=0.3,
        max_tokens=500
    )

    return response.choices[0].message.content
