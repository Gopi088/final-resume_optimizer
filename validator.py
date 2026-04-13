def find_missing_sections(data):
    expected = [
        "summary",
        "skills",
        "experience",
        "projects",
        "education"
    ]

    missing = []

    for sec in expected:
        if not data.get(sec):
            missing.append(sec)

    return missing