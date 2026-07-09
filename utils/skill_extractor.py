import re

# Expand this list later
SKILL_KEYWORDS = [
    "python", "java", "c++", "django", "flask", "sql", "mysql", "postgresql",
    "machine learning", "deep learning", "data analysis", "pandas", "numpy",
    "scikit-learn", "tensorflow", "pytorch", "html", "css", "javascript",
    "react", "git", "docker", "aws", "excel", "power bi", "tableau",
    "communication", "problem solving", "leadership", "recruitment",
    "talent acquisition", "employee relations", "hr analytics",
    "project management", "microsoft office suite"
]

def extract_skills(text):
    text = str(text).lower()
    found_skills = []

    for skill in SKILL_KEYWORDS:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text):
            found_skills.append(skill)
    
    return list(set(found_skills))