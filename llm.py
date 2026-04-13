import requests
import json

API_KEY = "your api key"


def rewrite_resume(data, jd_text):
    url = "https://api.deepseek.com/v1/chat/completions"

    prompt = f"""
You are a resume optimizer.

STRICT RULES:
- DO NOT remove any data
- DO NOT remove any section
- DO NOT rewrite name, education, certifications, skills
- DO NOT add new content
- DO NOT reduce number of points

ONLY:
- Improve summary wording
- Improve experience bullet points

IMPORTANT:
- Keep ALL original content
- Enhance wording only (no meaning change)

Return SAME JSON structure.

Resume JSON:
{json.dumps(data)}

Job Description:
{jd_text}
"""

    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    }

    headers = {
        "Authorization": f"Bearer {"sk-32f48dc7d23a4ec8b80cb8318bf36b67"}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=payload)

    try:
        result = response.json()
    except:
        print("❌ API error")
        print(response.text)
        return ""

    if "choices" not in result:
        print("❌ DeepSeek error:", result)
        return ""

    return result["choices"][0]["message"]["content"]