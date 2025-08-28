
import pandas as pd
from utils import load_data
from engine import preprocess_text, create_clusters, get_resume_score

# Load the data
DATA_PATH = '/data/UpdatedResumeDataSet.csv'
data = load_data(DATA_PATH)

# Preprocess the resume text
data['preprocessed_resume'] = data['Resume'].apply(preprocess_text)

# Create clusters
kmeans_model, vectorizer = create_clusters(data['preprocessed_resume'], num_clusters=5)

# Get the score for each resume
data['score'] = data['preprocessed_resume'].apply(lambda resume: get_resume_score(resume, kmeans_model, vectorizer))

# Print the data with scores
print(data.head())

# Save the model and vectorizer
import joblib
joblib.dump(kmeans_model, 'kmeans_model.joblib')
joblib.dump(vectorizer, 'vectorizer.joblib')
