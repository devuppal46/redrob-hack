import math
from typing import Dict, List
from models import JobDescription
from processor import normalize_and_dedupe

def calculate_idf(processed_resumes: Dict[str, List[str]], vocab: List[str]) -> Dict[str, float]:
    total_docs = len(processed_resumes)
    df_counts = {skill: 0 for skill in vocab}
    
    for skills in processed_resumes.values():
        for skill in set(skills):
            if skill in df_counts:
                df_counts[skill] += 1
                
    # Corrected: Applied smoothing to prevent zero division and zero weights
    return {skill: math.log((1 + total_docs) / (1 + count)) + 1 for skill, count in df_counts.items()}

def build_tfidf_vectors(processed_resumes: Dict[str, List[str]], vocab: List[str], idf: Dict[str, float]) -> Dict[str, List[float]]:
    vocab_index = {skill: i for i, skill in enumerate(vocab)}
    vectors = {}
    
    for r_id, skills in processed_resumes.items():
        skills_set = set(skills)
        n_skills = len(skills_set)
        tf = 1.0 / n_skills if n_skills > 0 else 0.0
        
        vector = [0.0] * len(vocab)
        for skill in skills_set:
            if skill in vocab_index:
                vector[vocab_index[skill]] = tf * idf[skill]
                
        vectors[r_id] = vector
    return vectors

def build_jd_vectors(job_descriptions: List[JobDescription], vocab: List[str]) -> Dict[str, List[float]]:
    vocab_index = {skill: i for i, skill in enumerate(vocab)}
    vectors = {}
    
    for jd in job_descriptions:
        skills_set = set(normalize_and_dedupe(jd.raw_skills))
        vector = [0.0] * len(vocab)
        for skill in skills_set:
            if skill in vocab_index:
                vector[vocab_index[skill]] = 1.0
        vectors[jd.id] = vector
    return vectors

def precompute_magnitudes(vectors: Dict[str, List[float]]) -> Dict[str, float]:
    return {v_id: math.sqrt(sum(val * val for val in vec)) for v_id, vec in vectors.items()}

def fast_cosine_similarity(vec_a: List[float], vec_b: List[float], mag_b_precomputed: float) -> float:
    dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
    mag_a = math.sqrt(sum(a * a for a in vec_a))
    
    if mag_a == 0.0 or mag_b_precomputed == 0.0:
        return 0.0
        
    return dot_product / (mag_a * mag_b_precomputed)