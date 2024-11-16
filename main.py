import os
import re
import PyPDF2
from tabulate import tabulate
import pandas as pd

def extract_text(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
        return ''

def extract_name(text):
    name_pattern = re.compile(r"\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)+\b")
    match = name_pattern.search(text)
    return match.group(0) if match else "Unknown"

def extract_contact(text):
    contact_pattern = re.compile(r"\+?\d{1,3}[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}")
    match = contact_pattern.search(text)
    return match.group(0) if match else "N/A"

def extract_email(text):
    email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    match = email_pattern.search(text)
    return match.group(0) if match else "N/A"

def extract_education(text):
    education_pattern = re.compile(r"\b(?:Bachelor|Master|PhD|CPD|Diploma|Degree)\b", re.IGNORECASE)
    match = education_pattern.search(text)
    return match.group(0) if match else "N/A"

def extract_skills(text):
    skills_pattern = re.compile(r"\b(?:Python|Java|JavaScript|C\+\+|HTML|CSS|React|Django|SQL)\b", re.IGNORECASE)
    matches = skills_pattern.findall(text)
    return list(set(matches)) if matches else []

def extract_experience(text):
    experience_pattern = re.compile(r"\b(?:Experience|Work history|Employment)\b.*(?:\d{4}|\b[A-Za-z]+)\b", re.IGNORECASE)
    match = experience_pattern.search(text)
    return match.group(0) if match else "Experience not extracted"

def parse_resume(file_path):
    text = extract_text(file_path)
    if not text:
        return {
            "Name": "Unknown",
            "Contact": "Unknown",
            "Email": "Unknown",
            "Education": "Unknown",
            "Skills": [],
            "Experience": "Experience not extracted"
        }
    
    name = extract_name(text)
    contact = extract_contact(text)
    email = extract_email(text)
    education = extract_education(text)
    skills = extract_skills(text)
    experience = extract_experience(text)

    return {
        "Name": name,
        "Contact": contact,
        "Email": email,
        "Education": education,
        "Skills": skills,
        "Experience": experience
    }

def display_parsed_data(parsed_data):
    headers = ["Name", "Contact", "Email", "Education", "Skills", "Experience"]
    rows = [[data["Name"], data["Contact"], data["Email"], data["Education"], ", ".join(data["Skills"]), data["Experience"]] for data in parsed_data]
    print(tabulate(rows, headers=headers, tablefmt="pretty"))

def save_to_excel(parsed_data, file_name="parsed_resumes.xlsx"):
    df = pd.DataFrame(parsed_data)
    df.to_excel(file_name, index=False)

def main():
    resume_files = ['resume.pdf']
    parsed_data = [parse_resume(resume_file) for resume_file in resume_files]
    display_parsed_data(parsed_data)
    save_to_excel(parsed_data)
    print("Resume parsing completed. Results saved.")

if __name__ == "__main__":
    main()



