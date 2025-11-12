import PyPDF2
import spacy
from collections import Counter
import sys

# Load spaCy language model (English)
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def extract_keywords(text):
    """
    Extract keywords and entities from text using spaCy
    Returns top 10 keywords
    """
    if not text or len(text) < 10:
        print("No valid text provided")
        return
    
    # Process text with spaCy
    doc = nlp(text.lower())
    
    # Extract named entities (ORG, PERSON, GPE, etc.)
    entities = [ent.text for ent in doc.ents 
                if ent.label_ in ["ORG", "PRODUCT", "GPE"]]
    
    # Extract noun phrases (useful skill indicators)
    keywords = []
    for token in doc:
        # Keep nouns, proper nouns, and verbs related to skills
        if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop and len(token.text) > 3:
            keywords.append(token.text)
    
    # Combine entities and keywords
    all_keywords = entities + keywords
    
    # Count frequency of each keyword
    keyword_freq = Counter(all_keywords)
    
    # Get top 10 most common keywords
    top_keywords = keyword_freq.most_common(10)
    
    # Display results
    print("\n" + "="*50)
    print("TOP 10 KEYWORDS FOUND:")
    print("="*50)
    for i, (keyword, count) in enumerate(top_keywords, 1):
        print(f"{i:2d}. {keyword.title():20s} - appeared {count} times")
    print("="*50 + "\n")

def main():
    """Main function to run the program"""
    print("\n" + "="*50)
    print("AI-POWERED RESUME KEYWORD EXTRACTOR")
    print("="*50 + "\n")
    
    while True:
        print("Choose an option:")
        print("1. Upload a PDF resume")
        print("2. Paste resume text")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1, 2, or 3): ").strip()
        
        if choice == "1":
            pdf_path = input("Enter the PDF file path: ").strip()
            try:
                with open(pdf_path, 'rb') as file:
                    resume_text = extract_text_from_pdf(file)
                    if "Error" not in resume_text:
                        print(f"\n✓ Successfully extracted text from {pdf_path}")
                        extract_keywords(resume_text)
                    else:
                        print(f"\n✗ {resume_text}")
            except FileNotFoundError:
                print(f"\n✗ File not found: {pdf_path}\n")
            except Exception as e:
                print(f"\n✗ Error: {str(e)}\n")
        
        elif choice == "2":
            print("\nPaste your resume text (enter 'END' on a new line when done):")
            lines = []
            while True:
                line = input()
                if line.strip().upper() == "END":
                    break
                lines.append(line)
            
            resume_text = "\n".join(lines)
            if resume_text.strip():
                extract_keywords(resume_text)
            else:
                print("\n✗ No text provided\n")
        
        elif choice == "3":
            print("\nThank you for using Resume Keyword Extractor. Goodbye!\n")
            break
        
        else:
            print("\n✗ Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()