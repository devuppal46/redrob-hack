from typing import NamedTuple

class Resume(NamedTuple):
    id: str
    name: str
    raw_skills: str

class JobDescription(NamedTuple):
    id: str
    company: str
    role: str
    raw_skills: str