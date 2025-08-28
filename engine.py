
import spacy

# Load the spacy model
nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    """
    Preprocesses the input text using spacy for more advanced NLP tasks.
    """
    doc = nlp(text.lower())
    tokens = []
    for token in doc:
        if not token.is_stop and not token.is_punct:
            if token.pos_ in ['NOUN', 'PROPN']:
                tokens.append(token.lemma_)
    return tokens


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def create_clusters(preprocessed_resumes, num_clusters=5):
    """
    Creates clusters of resumes using KMeans clustering.
    """
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([' '.join(resume) for resume in preprocessed_resumes])

    # Create a KMeans model
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(tfidf_matrix)

    return kmeans, vectorizer

def get_resume_score(preprocessed_resume, kmeans_model, vectorizer):
    """
    Calculates the score of a resume based on the trained KMeans model.
    """
    # Transform the resume into a TF-IDF vector
    tfidf_vector = vectorizer.transform([' '.join(preprocessed_resume)])

    # Predict the cluster
    cluster = kmeans_model.predict(tfidf_vector)[0]

    return cluster
