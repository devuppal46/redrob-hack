from models import Resume, JobDescription

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

RESUMES = [
    Resume("01", "Arjun Sharma", "Pyhton, MachineLearning, SQL, pandas, numpy, Deep-learning"),
    Resume("02", "Priya Nair", "JavaScrpit, Reacts, Node.JS, MongoDb, REST api, HTML/CSS"),
    Resume("03", "Rahul Gupta", "Java, Spring Boot, MySql, Microservices, Docker, kubernates"),
    Resume("04", "Sneha Patel", "Python, TensorFlow, Keras, NLP, BERT, data-viz, matplotlib"),
    Resume("05", "Vikram Singh", "C++, Algoritms, Data Structure, competitive programming, python"),
    Resume("06", "Ananya Krishnan", "javascript, vue.js, python, flask, PostgreSQL, AWS, CI/CD"),
    Resume("07", "Karan Mehta", "Python, Sklearn, XGboost, feature engineering, SQL, tableau"),
    Resume("08", "Deepika Rao", "Java, Android, Kotlin, Firebase, REST, UI/UX, figma"),
    Resume("09", "Aditya Kumar", "Reactjs, TypeScrpit, GraphQL, redux, tailwind, nodejs, jest"),
    Resume("10", "Meera Iyer", "python, R, statistics, ML, regression, clustering, Power-BI")
]

JOB_DESCRIPTIONS = [
    JobDescription("JD-1", "Kakao", "ML Engineer", "Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, SQL, Data Visualization, NLP, BERT, Feature Engineering, Statistics"),
    JobDescription("JD-2", "Naver", "Backend Engineer", "Java, Spring Boot, MySQL, PostgreSQL, Microservices, Docker, Kubernetes, REST API, CI/CD, Redis"),
    JobDescription("JD-3", "Line", "Frontend Engineer", "JavaScript, React, Vue, TypeScript, REST API, HTML/CSS, Node.js, GraphQL, Redux, Jest, AWS")
]