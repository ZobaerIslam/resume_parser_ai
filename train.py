import argparse
import pandas as pd
from utils import load_data
from engine import preprocess_text, create_clusters
import joblib

def train_model(data_path, num_clusters):
    """
    Train the KMeans model and TF-IDF vectorizer.
    """
    # Load the data
    data = load_data(data_path)

    # Preprocess the resume text
    data['preprocessed_resume'] = data['Resume'].apply(preprocess_text)

    # Create clusters
    kmeans_model, vectorizer = create_clusters(data['preprocessed_resume'], num_clusters=num_clusters)

    # Save the model and vectorizer
    joblib.dump(kmeans_model, 'kmeans_model.joblib')
    joblib.dump(vectorizer, 'vectorizer.joblib')

    print("Model trained and saved successfully.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train the resume parser model.')
    parser.add_argument('data_path', type=str, help='Path to the training data CSV file.')
    parser.add_argument('--num_clusters', type=int, default=5, help='Number of clusters to create.')
    args = parser.parse_args()

    train_model(args.data_path, args.num_clusters)
