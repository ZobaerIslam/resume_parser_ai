# Resume Parser AI

This project is a resume parser that uses AI to score resumes against a job description. It provides a web interface built with Streamlit to upload and analyze resumes.

## Features

- Parses resumes in PDF, DOCX and TXT format.
- Scores resumes against a job description using semantic similarity.
- Provides a user-friendly web interface to upload and analyze resumes.

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the web application, use the following command:

```bash
streamlit run app.py
```

This will start a local web server and open the application in your browser. You can then upload a resume file and a job description to see the matching score.

## File Descriptions

- `app.py`: The main file for the Streamlit web application.
- `engine.py`: Contains the core logic for parsing resumes and calculating the semantic similarity.
- `requirements.txt`: A list of the Python packages required to run the project.