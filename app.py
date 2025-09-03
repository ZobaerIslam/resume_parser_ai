import streamlit as st
import pandas as pd
import PyPDF2
import docx2txt
from engine import get_semantic_similarity

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

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>AI Resume Parser</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    uploaded_files = st.file_uploader("Upload your resumes", type=["pdf", "docx", "txt"], accept_multiple_files=True)

with col2:
    job_description = st.text_area("Enter the job description")

# Button to trigger scoring
if st.button("Get Score"):
    if uploaded_files is not None and job_description is not None:
        results = []
        for uploaded_file in uploaded_files:
            resume_text = read_resume_file(uploaded_file)
            if resume_text is not None:
                
                final_score = get_semantic_similarity(resume_text, job_description)

                results.append({"File Name": uploaded_file.name, "Score": final_score})

            else:
                st.error(f"Unsupported file type: {uploaded_file.name}")
        
        if results:
            df = pd.DataFrame(results)
            df = df.sort_values(by="Score", ascending=False)
            st.dataframe(df)
            st.info("The matching score is calculated based on the semantic similarity between your resume and the job description. It measures how well the meaning of the text in your resume aligns with the meaning of the text in the job description.")

    else:
        st.error("Please upload at least one resume and enter a job description.")