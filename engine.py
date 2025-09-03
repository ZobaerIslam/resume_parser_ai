from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')

def get_semantic_similarity(resume_text, job_description):
    """
    Calculates the semantic similarity between the resume and the job description.
    """
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_description_embedding = model.encode(job_description, convert_to_tensor=True)
    similarity_score = util.pytorch_cos_sim(resume_embedding, job_description_embedding)[0][0].item()
    return round(similarity_score * 10, 2)
