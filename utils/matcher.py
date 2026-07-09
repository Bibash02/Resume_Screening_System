import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import fuzz

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)  # Remove URLs
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters and numbers
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
    return text

def calculate_tfidf_similarity(resume_text, job_text):
    texts = [resume_text, job_text]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(similarity) * 100, 2

def calculate_skill_match(job_skills, resume_skills):
    job_set = set([str(skill).lower().strip() for skill in job_skills])
    resume_set = set([str(skill).lower().strip() for skill in resume_skills])

    matched_skills = sorted(job_set.intersection(resume_set))
    missing_skills = sorted(job_set - resume_set)

    if len(job_set) == 0:
        match_percentage = 0
    else:
        skill_score = (len(matched_skills) / len(job_set)) * 100
    return round(skill_score, 2), matched_skills, missing_skills

def calculate_fuzzy_skill_match(job_skills, resume_skills, threshold=80):
    job_skills_clean = [str(skill).lower().strip() for skill in job_skills]
    resume_skills_clean = [str(skill).lower().strip() for skill in resume_skills]

    matched_skills = []
    missing_skills = []

    for job_skill in job_skills_clean:
        found_match = False

        for resume_skill in resume_skills_clean:
            score = fuzz.ratio(job_skill, resume_skill)
            if score >= threshold:
                matched_skills.append(job_skill)
                found_match = True
                break
        
        if not found_match:
            missing_skills.append(job_skill)
    
    if len(job_skills_clean) == 0:
        fuzzy_score = 0
    else:
        fuzzy_score = (len(matched_skills) / len(job_skills_clean)) * 100

    return round(fuzzy_score, 2), sorted(set(matched_skills)), sorted(set(missing_skills))

def calculate_final_score(tfidf_score, skill_score, fuzzy_score):
    final_score = (
        0.30 * tfidf_score +
        0.35 * skill_score +
        0.35 * fuzzy_score
    )
    return round(final_score, 2)

def match_resume_to_job(resume_text, job_text, job_skills, resume_skills):
    resume_text_clean = clean_text(resume_text)
    job_text_clean = clean_text(job_text)

    tfidf_score = calculate_tfidf_similarity(resume_text_clean, job_text_clean)

    skill_score, exact_matched_skills, exact_matched_skills = calculate_skill_match(job_skills, resume_skills)

    fuzzy_score, fuzzy_matched_skills, fuzzy_missing_skills = calculate_fuzzy_skill_match(job_skills, resume_skills)

    final_score = calculate_final_score(tfidf_score, skill_score, fuzzy_score)

    return {
        "tfidf_score": tfidf_score,
        "excact_skill_score": skill_score,
        "fuzzy_skill_score": fuzzy_score,
        "final_score": final_score,
        "matched_skills": fuzzy_matched_skills,
        "missing_skills": fuzzy_missing_skills
    } 
    

