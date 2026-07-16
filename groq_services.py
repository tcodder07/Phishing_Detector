import os
from dotenv import load_dotenv
from groq import Groq
from utiles.url_extractor import extract_urls

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_message(message):
    urls = extract_urls(message)

    prompt = f"""
You are a cybersecurity expert.

Analyze the following email or SMS.

Return ONLY in this format:

Verdict:
Risk Score:
Reasons:
Recommended Action:

Message:
{message}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a cybersecurity expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return {
        "urls_found": urls,
        "ai_analysis": response.choices[0].message.content
    }