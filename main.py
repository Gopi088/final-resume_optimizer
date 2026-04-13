import os
import json
from parser import extract_text
from extractor import extract_resume_structure
from llm import rewrite_resume
from formatter import generate_pdf


def clean_llm_output(output):
    output = output.strip()

    if output.startswith("```"):
        output = output.split("```")[1]
        if output.strip().startswith("json"):
            output = output.strip()[4:]

    return output.strip()


# 🔥 Fallback name extractor
def extract_name_from_text(resume_text):
    lines = resume_text.strip().split("\n")

    for line in lines:
        line = line.strip()
        if len(line) > 2 and len(line.split()) <= 4:
            return line

    return "Unknown Candidate"


# 🔥 SAFE MERGE (CRITICAL)
def merge_data(original, updated, resume_text):
    for key in original:
        if key not in updated or not updated[key]:
            updated[key] = original[key]

    # 🔥 Force name
    if not updated.get("name"):
        updated["name"] = original.get("name") or extract_name_from_text(resume_text)

    # 🔥 Preserve experience
    if "experience" in original:
        for i in range(len(original["experience"])):
            if i >= len(updated["experience"]):
                updated["experience"].append(original["experience"][i])
            else:
                orig_points = original["experience"][i].get("points", [])
                new_points = updated["experience"][i].get("points", [])

                if len(new_points) < len(orig_points):
                    updated["experience"][i]["points"] = orig_points

    return updated


def get_resume_with_confirmation():
    while True:
        path = input("📄 Enter resume file (name or path): ").strip().strip('"')

        if not os.path.exists(path):
            alt_path = os.path.join(os.getcwd(), path)
            if os.path.exists(alt_path):
                path = alt_path
            else:
                print("❌ File not found. Try again.\n")
                continue

        print(f"\n👉 You selected: {path}")
        print("1. Continue")
        print("2. Change path")

        choice = input("Select option (1 or 2): ").strip()

        if choice == "1":
            return path
        elif choice == "2":
            print("\n🔁 Re-enter resume path\n")
        else:
            print("❌ Invalid choice\n")


def get_jd_input():
    print("\nChoose JD input method:")
    print("1. Paste JD text")
    print("2. Provide JD file")

    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "1":
        print("\n📋 Paste Job Description (press ENTER twice to finish):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        return "\n".join(lines)

    elif choice == "2":
        while True:
            jd_path = input("📄 Enter JD file (name or path): ").strip().strip('"')

            # Handle folder
            if os.path.isdir(jd_path):
                files = os.listdir(jd_path)
                valid_files = [f for f in files if f.endswith((".pdf", ".docx", ".txt"))]

                if not valid_files:
                    print("❌ No valid JD files found.\n")
                    continue

                print("\n📂 Files:")
                for i, f in enumerate(valid_files, 1):
                    print(f"{i}. {f}")

                choice = input("Select file number: ").strip()

                if choice.isdigit() and 1 <= int(choice) <= len(valid_files):
                    selected = valid_files[int(choice) - 1]
                    return extract_text(os.path.join(jd_path, selected))

                print("❌ Invalid selection.\n")
                continue

            if os.path.isfile(jd_path):
                return extract_text(jd_path)

            print("❌ File/Folder not found. Try again.")

    else:
        print("❌ Invalid choice.")
        return get_jd_input()


def generate_output_filename(resume_path):
    base_name = os.path.basename(resume_path)
    name = os.path.splitext(base_name)[0]
    return f"output/{name}_optimized.pdf"


def main():
    print("🚀 Resume Optimizer Started\n")

    # Step 1: Resume
    resume_path = get_resume_with_confirmation()
    resume_text = extract_text(resume_path)

    # Step 2: JD
    jd_text = get_jd_input()

    # =========================
    # STEP 1: EXTRACT
    # =========================
    print("\n🧠 Extracting resume...")
    raw_json = extract_resume_structure(resume_text)

    if not raw_json:
        print("❌ Extraction failed")
        return

    cleaned = clean_llm_output(raw_json)

    try:
        data = json.loads(cleaned)
    except Exception as e:
        print("❌ Extraction JSON error")
        print(e)
        return

    # =========================
    # STEP 2: REWRITE
    # =========================
    print("\n🤖 Optimizing resume...")
    optimized_json = rewrite_resume(data, jd_text)

    if not optimized_json:
        print("❌ Rewrite failed")
        return

    cleaned = clean_llm_output(optimized_json)

    try:
        updated_data = json.loads(cleaned)
    except Exception as e:
        print("❌ Rewrite JSON error")
        print(e)
        return

    # 🔥 Merge fix
    data = merge_data(data, updated_data, resume_text)

    # =========================
    # OUTPUT
    # =========================
    os.makedirs("output", exist_ok=True)
    output_file = generate_output_filename(resume_path)

    print("📄 Generating PDF...")
    generate_pdf(data, output_file)

    print(f"\n✅ Done! Saved at: {output_file}")


if __name__ == "__main__":
    main()