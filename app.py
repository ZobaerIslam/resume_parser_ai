
import streamlit as st
import pandas as pd
import PyPDF2
import docx2txt
import joblib
from engine import preprocess_text
from sklearn.metrics.pairwise import cosine_similarity

# Load the trained model and vectorizer
vectorizer = joblib.load('vectorizer.joblib')
kmeans_model = joblib.load('kmeans_model.joblib')

def read_resume_file(file):
    """
    Reads the content of the uploaded resume file.
    """
    if file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return docx2txt.process(file)
    elif file.type == "text/plain":
        return file.read().decode("utf-8")
    else:
        return None

st.title("AI Resume Parser")

# File uploader
uploaded_files = st.file_uploader("Upload your resumes", type=["pdf", "docx", "txt"], accept_multiple_files=True)

# Text area for job description
job_description = st.text_area("Enter the job description")

# Button to trigger scoring
if st.button("Get Score"):
    if uploaded_files is not None and job_description is not None:
        results = []
        for uploaded_file in uploaded_files:
            resume_text = read_resume_file(uploaded_file)
            if resume_text is not None:
                # Preprocess the job description and resume text
                preprocessed_job_description = preprocess_text(job_description)
                preprocessed_resume = preprocess_text(resume_text)

                # Transform the text into TF-IDF vectors
                job_description_vector = vectorizer.transform([' '.join(preprocessed_job_description)])
                resume_vector = vectorizer.transform([' '.join(preprocessed_resume)])

                # Calculate the cosine similarity
                similarity_score = cosine_similarity(job_description_vector, resume_vector)[0][0]

                # Convert the score to a scale of 0-10
                final_score = round(similarity_score * 10, 2)

                results.append({"File Name": uploaded_file.name, "Score": final_score})
            else:
                st.error(f"Unsupported file type: {uploaded_file.name}")
        
        if results:
            st.dataframe(pd.DataFrame(results))

    else:
        st.error("Please upload at least one resume and enter a job description.")
