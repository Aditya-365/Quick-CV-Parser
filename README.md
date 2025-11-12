Resume Extractor

A simple and efficient Python CLI tool that extracts key information from resumes using Natural Language Processing (NLP) with spaCy.

This project allows users to upload or paste resume text and automatically identifies details like names, emails, phone numbers, skills, and more — all through a clean command-line interface.

Features

Extracts structured information (name, contact info, skills, etc.) from unstructured resumes

Works with both PDF files and plain text input

Built with spaCy NLP for entity recognition

Lightweight, fast, and easy to use

⚙️ How to Use It

Getting this up and running is pretty straightforward.

1️. Set Up Your Environment

It’s best to use a Python virtual environment (venv) to keep dependencies tidy.

# Create a virtual environment
python -m venv venv

# Activate it (on Mac/Linux)
source venv/bin/activate

# Or on Windows
.\venv\Scripts\activate

2️. Install Dependencies

All required libraries are listed in requirements.txt. Install them with:

pip install -r requirements.txt

3️. Download the spaCy Language Model

The project relies on spaCy’s pre-trained English model. Download it by running:

python -m spacy download en_core_web_sm

4️. Run the Script!

Once everything is set up, just run the main file:

python resume_extractor.py


You’ll be greeted with a menu offering three options:

Upload a PDF resume — Enter the path to your PDF file.

Paste resume text — Paste your text directly into the terminal.
(When finished, type END on a new line and press Enter.)

Exit — Quit the program.

Tech Stack

Python 3.8+

PyPDF2 – PDF text extraction

spaCy – NLP-based keyword and entity recognition

CLI-based interaction
