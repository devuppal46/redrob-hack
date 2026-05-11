from constants import RESUMES, JOB_DESCRIPTIONS
from processor import normalize_and_dedupe, build_vocabulary
from scoring import (
    calculate_idf, 
    build_tfidf_vectors, 
    build_jd_vectors, 
    precompute_magnitudes, 
    fast_cosine_similarity
)

def run_pipeline():
    processed_resumes = {r.id: normalize_and_dedupe(r.raw_skills) for r in RESUMES}
    
    vocabulary = build_vocabulary(processed_resumes)
    idf_scores = calculate_idf(processed_resumes, vocabulary)
    
    resume_vectors = build_tfidf_vectors(processed_resumes, vocabulary, idf_scores)
    jd_vectors = build_jd_vectors(JOB_DESCRIPTIONS, vocabulary)
    
    jd_magnitudes = precompute_magnitudes(jd_vectors)
    
    for jd in JOB_DESCRIPTIONS:
        scores = []
        for r in RESUMES:
            score = fast_cosine_similarity(
                resume_vectors[r.id], 
                jd_vectors[jd.id], 
                jd_magnitudes[jd.id]
            )
            scores.append({"name": r.name, "score": score})
            
        scores.sort(key=lambda x: (-x["score"], x["name"]))
        
        top_3 = scores[:3]
        formatted = ", ".join([f"{c['name']}({c['score']:.2f})" for c in top_3])
        
        print(f"{jd.id} - {jd.company} ({jd.role})")
        print(formatted)
        print()

if __name__ == "__main__":
    run_pipeline()