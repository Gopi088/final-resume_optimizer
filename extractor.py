import requests
import json

API_KEY = "your api key"


def extract_resume_structure(resume_text):
    url = "https://api.deepseek.com/v1/chat/completions"

    prompt = f"""
Extract structured data from resume.

STRICT RULES:
- DO NOT rewrite
- DO NOT summarize
- DO NOT remove anything
- Copy exact data

Return JSON:

{{
  "name": "",
  "title": "",
  "contact": "",
  "summary": "",
  "skills": [],
  "certifications": [],
  "education": [],
  "experience": [
    {{
      "role": "",
      "company": "",
      "points": []
    }}
  ]
}}

Resume:
{resume_text}
"""

    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0
    }

    headers = {
        "Authorization": f"Bearer {"sk-32f48dc7d23a4ec8b80cb8318bf36b67"}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()

    return result["choices"][0]["message"]["content"]