import math

SKILL_ALIASES = {
    "python": "python", "pyhton": "python", "java": "java", "javascript": "javascript",
    "javascrpit": "javascript", "js": "javascript", "typescript": "typescript",
    "typescrpit": "typescript", "c++": "cpp", "cpp": "cpp", "r": "r", "kotlin": "kotlin",
    "machinelearning": "machine_learning", "machine learning": "machine_learning",
    "ml": "machine_learning", "sklearn": "machine_learning", "deeplearning": "deep_learning",
    "deep learning": "deep_learning", "deep-learning": "deep_learning", "tensorflow": "tensorflow",
    "pytorch": "pytorch", "keras": "keras", "nlp": "nlp", "bert": "bert", "xgboost": "xgboost",
    "feature engineering": "feature_engineering", "statistics": "statistics", "stats": "statistics",
    "regression": "regression", "clustering": "clustering", "data-viz": "data_visualization",
    "data visualization": "data_visualization", "data viz": "data_visualization",
    "matplotlib": "data_visualization", "tableau": "data_visualization", "power-bi": "data_visualization",
    "power bi": "data_visualization", "powerbi": "data_visualization", "pandas": "pandas",
    "numpy": "numpy", "react": "react", "reacts": "react", "reactjs": "react", "vue": "vue",
    "vue.js": "vue", "vuejs": "vue", "redux": "redux", "tailwind": "tailwind", "html/css": "html_css",
    "html css": "html_css", "html": "html_css", "css": "html_css", "jest": "jest",
    "graphql": "graphql", "node.js": "nodejs", "nodejs": "nodejs", "node js": "nodejs",
    "flask": "flask", "spring boot": "spring_boot", "springboot": "spring_boot",
    "rest api": "rest_api", "rest": "rest_api", "restapi": "rest_api", "microservices": "microservices",
    "sql": "sql", "mysql": "mysql", "mysq": "mysql", "postgresql": "postgresql",
    "postgres": "postgresql", "mongodb": "mongodb", "redis": "redis", "docker": "docker",
    "kubernetes": "kubernetes", "kubernates": "kubernetes", "k8s": "kubernetes", "ci/cd": "ci_cd",
    "cicd": "ci_cd", "ci cd": "ci_cd", "aws": "aws", "android": "android", "firebase": "firebase",
    "algorithms": "algorithms", "algoritms": "algorithms", "data structure": "data_structures",
    "data structures": "data_structures", "competitive programming": "competitive_programming",
    "ui/ux": "ui_ux", "ui ux": "ui_ux", "figma": "figma",
}

RESUMES = {
    "01": {"name": "Arjun Sharma", "skills": "Pyhton, MachineLearning, SQL, pandas, numpy, Deep-learning"},
    "02": {"name": "Priya Nair", "skills": "JavaScrpit, Reacts, Node.JS, MongoDb, REST api, HTML/CSS"},
    "03": {"name": "Rahul Gupta", "skills": "Java, Spring Boot, MySql, Microservices, Docker, kubernates"},
    "04": {"name": "Sneha Patel", "skills": "Python, TensorFlow, Keras, NLP, BERT, data-viz, matplotlib"},
    "05": {"name": "Vikram Singh", "skills": "C++, Algoritms, Data Structure, competitive programming, python"},
    "06": {"name": "Ananya Krishnan", "skills": "javascript, vue.js, python, flask, PostgreSQL, AWS, CI/CD"},
    "07": {"name": "Karan Mehta", "skills": "Python, Sklearn, XGboost, feature engineering, SQL, tableau"},
    "08": {"name": "Deepika Rao", "skills": "Java, Android, Kotlin, Firebase, REST, UI/UX, figma"},
    "09": {"name": "Aditya Kumar", "skills": "Reactjs, TypeScrpit, GraphQL, redux, tailwind, nodejs, jest"},
    "10": {"name": "Meera Iyer", "skills": "python, R, statistics, ML, regression, clustering, Power-BI"}
}

JOB_DESCRIPTIONS = {
    "JD-1": {"company": "Kakao", "role": "ML Engineer", "skills": "Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, SQL, Data Visualization, NLP, BERT, Feature Engineering, Statistics"},
    "JD-2": {"company": "Naver", "role": "Backend Engineer", "skills": "Java, Spring Boot, MySQL, PostgreSQL, Microservices, Docker, Kubernetes, REST API, CI/CD, Redis"},
    "JD-3": {"company": "Line", "role": "Frontend Engineer", "skills": "JavaScript, React, Vue, TypeScript, REST API, HTML/CSS, Node.js, GraphQL, Redux, Jest, AWS"}
}

def normalize_skills(raw_skills_str):
    tokens = [s.strip().lower() for s in raw_skills_str.split(',')]
    normalized = []
    for token in tokens:
        if token in SKILL_ALIASES:
            normalized.append(SKILL_ALIASES[token])
    return normalized

def deduplicate_skills(skills_list):
    return list(dict.fromkeys(skills_list))

for r_id, r_data in RESUMES.items():
    raw = r_data["skills"]
    norm_dedup = deduplicate_skills(normalize_skills(raw))
    RESUMES[r_id]["processed_skills"] = norm_dedup

for j_id, j_data in JOB_DESCRIPTIONS.items():
    raw = j_data["skills"]
    norm_dedup = deduplicate_skills(normalize_skills(raw))
    JOB_DESCRIPTIONS[j_id]["processed_skills"] = norm_dedup

all_resume_skills = []
for r in RESUMES.values():
    all_resume_skills.extend(r["processed_skills"])

vocabulary = sorted(list(set(all_resume_skills)))
TOTAL_DOCS = len(RESUMES)

df_counts = {skill: 0 for skill in vocabulary}
for r in RESUMES.values():
    for skill in set(r["processed_skills"]):
        df_counts[skill] += 1

idf_scores = {}
for skill in vocabulary:
    idf_scores[skill] = math.log(TOTAL_DOCS / df_counts[skill])

def build_tfidf_vector(processed_skills, vocab, idf_dict):
    vector = [0.0] * len(vocab)
    if not processed_skills:
        return vector
    
    tf = 1.0 / len(processed_skills)
    
    for skill in processed_skills:
        if skill in vocab:
            idx = vocab.index(skill)
            vector[idx] = tf * idf_dict[skill]
    return vector

for r_id, r_data in RESUMES.items():
    r_data["vector"] = build_tfidf_vector(r_data["processed_skills"], vocabulary, idf_scores)


def build_jd_binary_vector(processed_skills, vocab):
    vector = [0.0] * len(vocab)
    for skill in processed_skills:
        if skill in vocab:
            idx = vocab.index(skill)
            vector[idx] = 1.0
    return vector

def cosine_similarity(vec_a, vec_b):
    dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
    mag_a = math.sqrt(sum(a * a for a in vec_a))
    mag_b = math.sqrt(sum(b * b for b in vec_b))
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return dot_product / (mag_a * mag_b)

for j_id, j_data in JOB_DESCRIPTIONS.items():
    j_data["vector"] = build_jd_binary_vector(j_data["processed_skills"], vocabulary)

results = {j_id: [] for j_id in JOB_DESCRIPTIONS.keys()}

for j_id, j_data in JOB_DESCRIPTIONS.items():
    for r_id, r_data in RESUMES.items():
        score = cosine_similarity(r_data["vector"], j_data["vector"])
        results[j_id].append({"name": r_data["name"], "score": score})


for j_id, candidates in results.items():
    candidates.sort(key=lambda x: (-x["score"], x["name"]))
    
    company = JOB_DESCRIPTIONS[j_id]["company"]
    role = JOB_DESCRIPTIONS[j_id]["role"]
    top_3 = candidates[:3]
    
    formatted_top_3 = ", ".join([f"{c['name']}({c['score']:.2f})" for c in top_3])
    print(f"{j_id} - {company} ({role})")
    print(formatted_top_3)
    print()