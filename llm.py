import requests
import json
import time
from config import API_KEY, BASE_URL, MODEL


def safe_request(url, headers, payload, retries=3):
    for attempt in range(retries):
        try:
            print(f"📦 Payload size: {len(json.dumps(payload))} characters")

            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=120  # 🔥 Increased timeout
            )

            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"⚠️ Retry {attempt + 1}: {e}")
            time.sleep(2)

    print("❌ API failed after retries")
    return None


def rewrite_resume(resume_data, jd_text):
    """
    🔥 Optimizes ONLY summary + experience
    Prevents large payload → avoids timeout
    """

    # 🔥 Extract only needed parts (VERY IMPORTANT)
    summary = resume_data.get("summary", "")
    experience = resume_data.get("experience", [])

    # 🔥 Limit JD size to avoid timeout
    jd_text_limited = jd_text[:3000]

    prompt = f"""
You are an expert resume optimizer.

STRICT RULES:
- Do NOT remove ANY content
- Do NOT skip ANY section
- Improve ONLY summary and experience
- Do NOT change structure
- Do NOT remove projects, awards, achievements
- Do NOT add fake data

Return JSON format:
{{
  "summary": "",
  "experience": [
    {{
      "role": "",
      "company": "",
      "points": []
    }}
  ]
}}

Resume Summary:
{summary}

Experience:
{json.dumps(experience)}

Job Description:
{jd_text_limited}
"""

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    result = safe_request(BASE_URL, headers, payload)

    if not result or "choices" not in result:
        return None

    return result["choices"][0]["message"]["content"]