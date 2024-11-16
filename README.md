# Resume Parser

This project is a Python-based Resume Parser that extracts key information such as Name, Contact, Email, Education, Skills, and Experience from a given resume PDF file. The extracted data is then displayed in a well-structured table format and saved as an Excel file for further analysis.

## Features
- Extracts text data from resume PDF files.
- Parses key sections such as Name, Contact, Email, Education, Skills, and Experience.
- Displays the parsed data in a formatted table.
- Saves the extracted data to an Excel file.

## Prerequisites

Before running the project, ensure you have the following Python libraries installed:

- `PyPDF2` for extracting text from PDF files.
- `re` (Regular Expression) for parsing and extracting relevant information from the resume.
- `pandas` for data handling and exporting data to Excel.
- `tabulate` for formatting and displaying data in the terminal.

You can install these dependencies using the following command:

```bash
pip install -r requirements.txt
