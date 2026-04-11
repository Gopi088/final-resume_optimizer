# 🚀 Resume Optimizer (AI-Powered CLI Tool)

An AI-based command-line tool that rewrites resumes based on a Job Description (JD) using DeepSeek, while ensuring:

* ✅ No data loss
* ✅ No fake content
* ✅ Original structure is preserved
* ✅ Works with multiple file formats
* ✅ Outputs a clean, professional PDF

---

# 📌 Features

* 📄 Supports **PDF, DOCX, TXT, Images (OCR)**
* 🧠 AI-powered resume optimization using DeepSeek
* 🔒 Strict rules to **prevent hallucination**
* 🧩 Preserves original sections (no forced sections)
* 🎯 Tailors resume based on JD keywords
* 🖨️ Generates formatted **PDF output**
* 💻 Fully CLI-based (Linux/WSL compatible)
* 🔁 Editable input (confirm/change resume path)

---

# 🏗️ Project Structure

```
resume_optimizer/
│
├── main.py           # CLI entry point
├── parser.py         # Resume & JD parsing
├── llm.py            # DeepSeek API integration
├── formatter.py      # HTML → PDF generator
├── template.html     # Resume template
├── requirements.txt  # Python dependencies
├── Dockerfile        # Docker setup
└── output/           # Generated resumes
```

---

# ⚙️ Setup Instructions (Linux / WSL)

## 1️⃣ Install system dependencies

```bash
sudo apt update
sudo apt install -y python3-pip tesseract-ocr wkhtmltopdf
```

---

## 2️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure API Key

Update `llm.py` OR (recommended) use environment variable:

```bash
export DEEPSEEK_API_KEY="your_api_key_here"
```

And in `llm.py`:

```python
import os
API_KEY = os.getenv("DEEPSEEK_API_KEY")
```

---

# ▶️ Usage

Run the application:

```bash
python main.py
```

---

# 🧑‍💻 CLI Workflow

### Step 1: Enter Resume

```
📄 Enter resume file:
resume.pdf
```

---

### Step 2: Confirm or Change Path

```
👉 You selected: /path/resume.pdf
1. Continue
2. Change path
```

---

### Step 3: Provide Job Description

```
Choose JD input method:
1. Paste JD text
2. Provide JD file
```

---

### Step 4: Processing

```
🤖 Optimizing resume...
📄 Generating PDF...
```

---

### ✅ Output

```
output/resume_optimized.pdf
```

---

# 🧠 How It Works

1. Extracts text from resume (PDF/DOCX/Image via OCR)
2. Extracts JD (file or pasted input)
3. Sends structured prompt to DeepSeek
4. Ensures:

   * No data loss
   * No section creation
   * No fake content
5. Receives optimized JSON
6. Converts JSON → HTML → PDF

---

# 🔒 Design Principles

* ❌ No hallucinated content
* ❌ No forced sections
* ❌ No data removal
* ✅ Only improves wording
* ✅ Preserves structure
* ✅ Works with any resume

---

# ⚠️ Important Notes

* Large inputs are trimmed automatically (API limits)
* Ensure `wkhtmltopdf` is installed
* OCR requires `tesseract-ocr`
* Works best with structured resumes

---

# 🛠️ Troubleshooting

## ❌ KeyError: 'choices'

* API failed
* Check:

  * API key
  * internet connection
  * input size

---

## ❌ JSON parsing error

* LLM returned invalid JSON
* Check prompt or API response

---

## ❌ Weird characters in PDF

* Fixed using UTF-8 encoding
* Ensure latest `template.html` is used

---

## ❌ File not found

* Use correct path
* Supports:

  * full path
  * relative path
  * current directory

---

# 🐳 Docker Setup

## Build image

```bash
docker build -t resume-optimizer .
```

---

## Run container

```bash
docker run -it resume-optimizer
```

---

## Run with file access

```bash
docker run -it -v $(pwd):/app resume-optimizer
```

---

# 🚀 Deployment

You can run this project on:

* 🖥️ Local machine (recommended)
* ☁️ AWS EC2
* ☁️ Azure VM
* ☁️ Google Cloud VM

---

# 📦 requirements.txt

```
pymupdf
python-docx
pytesseract
pillow
jinja2
pdfkit
requests
```

---

# 🎯 Example

**Input:**

* Resume: `resume.pdf`
* JD: `jd.docx` or pasted text

**Output:**

```
output/resume_optimized.pdf
```

---

# 🚀 Future Improvements

* 📊 ATS score calculation
* 🎯 JD vs Resume match %
* 🔍 Resume comparison (before vs after)
* ⚡ Batch processing
* 🖼️ Logo-based certification rendering
* 🌐 Web UI version

---

# 👨‍💻 Author Notes

This tool is designed to be:

* Simple
* Flexible
* Safe (no data loss)
* Production-ready

---

# ⭐ Pro Tip

For best results:

* Use well-structured resumes
* Provide clear job descriptions
* Avoid extremely large files

---

# 🏁 You're Ready!

Run the tool and generate optimized resumes 🚀
