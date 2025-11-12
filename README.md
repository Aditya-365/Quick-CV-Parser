# 🧠 Resume Extractor

A simple and efficient **Python CLI tool** that extracts key information from resumes using **Natural Language Processing (NLP)** with **spaCy**.

---

## ⚙️ How to Use It

Getting this up and running is straightforward.

### 1️. Set Up Your Environment

It’s best to use a **Python virtual environment (venv)** to keep dependencies tidy.

```bash
# Create a virtual environment
python -m venv venv
bash
Copy code
# Activate it (on Mac/Linux)
source venv/bin/activate
bash
Copy code
# Or on Windows
.\venv\Scripts\activate
```
2️. Install Dependencies
All required libraries are listed in requirements.txt. Install them with:

bash
Copy code
pip install -r requirements.txt
3️. Download the spaCy Language Model
The script relies on spaCy’s pre-trained English language model. Download it by running:

bash
Copy code
python -m spacy download en_core_web_sm
4️. Run the Script
Once everything is installed, just run the main file:

bash
Copy code
python resume_extractor.py
From there, the script will greet you and give you three choices:

Upload a PDF resume — Enter the file path to your PDF.

Paste resume text — Paste your text directly into the terminal.
(When done, type END on a new, empty line and press Enter.)

Exit — Quit the program.

🧩 Tech Stack
Python 3.8+

PyPDF2 – For PDF text extraction

spaCy – For NLP-based keyword and entity recognition

Command-line Interface (CLI)

