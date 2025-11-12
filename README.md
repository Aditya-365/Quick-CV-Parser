# **Quick-CV-Parser**

### **AI-Powered Resume Keyword Extractor**

Hey there! Thanks for checking out my **Resume Keyword Extractor** project.

I built this little command-line tool because I wanted a fast and simple way to scan a resume (either a PDF or plain text) and instantly see the most important and frequently mentioned terms.  

Whether you're a **recruiter** trying to get a quick snapshot of a candidate or a **job-seeker** wanting to see what keywords stand out in your own resume, I'm hoping this tool can help you out.

---

## **What It Does**

This script is a simple, interactive tool that runs right in your terminal. Here's a quick breakdown of what's happening under the hood:

- **Two Ways to Input**  
  You can either provide a direct file path to a **PDF resume** or simply copy and paste the **full text** of a resume directly into the terminal.

- **PDF Text Extraction**  
  If you provide a PDF, it uses the **PyPDF2** library to read the file and extract all the text from its pages.

- **NLP Magic (with spaCy)**  
  Once it has the text, the script feeds it into the **spaCy** natural language processing (NLP) library.

- **Keyword & Entity Analysis**  
  The script is configured to:  
  - Identify important Named Entities like **Organizations (ORG)**, **Products (PRODUCT)**, and **Locations (GPE)**.  
  - Pull out key **Nouns** and **Proper Nouns** (like *“Python,” “Engineering,” or “Management”*).  
  - Filter out common, non-important **stop words** (like *‘the’, ‘is’, ‘a’, ‘and’*) to keep results clean.

- **Top 10 List**  
  It counts the frequency of all these extracted keywords and entities, then presents a clean **Top 10** list showing which terms appeared most often.

---

## **How to Use It**

Getting this up and running is pretty straightforward.

### **1️. Set Up Your Environment**

I recommend using a **Python virtual environment (venv)** to keep dependencies tidy.

```bash
# Create a virtual environment
python -m venv venv

# Activate it (on Mac/Linux)
source venv/bin/activate

# Or on Windows
.\venv\Scripts\activate
