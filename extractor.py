import requests
import json
from config import API_KEY, BASE_URL, MODEL


def extract_resume_structure(resume_text):
    prompt = f"""
Extract ALL information from the resume.

STRICT RULES:
- DO NOT rewrite
- DO NOT summarize
- Capture ALL sections
- If section unknown → put in "extra_sections"

Return JSON:

{{
  "name": "",
  "title": "",
  "contact": "",
  "summary": "",
  "skills": [],
  "education": [],
  "certifications": [],
  "experience": [
    {{
      "role": "",
      "company": "",
      "points": []
    }}
  ],
  "projects": [],
  "awards": [],
  "achievements": [],
  "publications": [],
  "extra_sections": {{}}
}}

Resume:
{resume_text}
"""

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",   # ✅ FIXED
        "Content-Type": "application/json"
    }

    response = requests.post(BASE_URL, headers=headers, json=payload)
    result = response.json()

    return result["choices"][0]["message"]["content"]