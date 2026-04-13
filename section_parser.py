import re

COMMON_SECTIONS = {
    "summary": ["summary", "profile", "about"],
    "skills": ["skills", "technical skills", "core skills"],
    "experience": ["experience", "work experience", "employment"],
    "projects": ["project", "projects"],
    "education": ["education", "academic"],
    "certifications": ["certification", "certifications"],
    "achievements": ["achievement", "awards", "recognition"]
}


def detect_section(line):
    line = line.lower()

    for section, keywords in COMMON_SECTIONS.items():
        for keyword in keywords:
            if keyword in line:
                return section

    return None


def split_sections(text):
    sections = {}
    current_section = "other"

    for line in text.split("\n"):
        clean_line = line.strip()

        if not clean_line:
            continue

        detected = detect_section(clean_line)

        if detected:
            current_section = detected

        sections.setdefault(current_section, []).append(clean_line)

    return sections