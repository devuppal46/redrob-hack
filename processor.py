from typing import Dict, List
from constants import SKILL_ALIASES

def normalize_and_dedupe(raw_skills: str) -> List[str]:
    tokens = [t.strip().lower() for t in raw_skills.split(',')]
    return list(dict.fromkeys(
        SKILL_ALIASES[token] for token in tokens if token in SKILL_ALIASES
    ))

def build_vocabulary(processed_resumes: Dict[str, List[str]]) -> List[str]:
    return sorted(set(skill for skills in processed_resumes.values() for skill in skills))