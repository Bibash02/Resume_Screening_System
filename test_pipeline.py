from utils.resume_parser import extract_resume_text
from utils.role_predictor import predict_role
from utils.skill_extractor import extract_skills
from utils.matcher import match_resume_to_job

# path to a sample resume file
resume_file_path = "uploads/resumes/sample_resume.txt"

# sample job description
job_text = """
We are hiring a Python Developer with experience in Flask, Django, REST APIs,
SQL, Git, Docker, AWS, problem solving, and communication skills.
"""

job_skills = [
    "python",
    "django",
    "flask",
    "rest apis",
    "sql",
    "git",
    "docker",
    "aws",
    "problem solving",
    "communication"
]

# extract resume text
resume_text = extract_resume_text(resume_file_path)

print("=" * 60)
print("Resume Text Preview")
print("=" * 60)
print(resume_text[:1000])  # show first 1000 characters

# predict role
predicted_role = predict_role(resume_text)

print("\n" + "=" * 60)
print("Predicted Role")
print("=" * 60)
print(predicted_role)

# extracts resume skills
resume_skills = extract_skills(resume_text)

print("=" * 60)
print("Extracted Resume Skills")
print("=" * 60)
print(resume_skills)

# match resume to job
result = match_resume_to_job(resume_text = resume_text, job_text=job_text, job_skills=job_skills, resume_skills=resume_skills)

print("\n" + "=" * 60)
print("Matching Result")
print("=" * 60)
print("TF-IDF Score:", result["tfidf_score"])
print("Exact skill score:", result["exact_skill_score"])
print("Fuzzy Skill Score:", result["fuzzy_skill_score"])
print("Final match score:", result["final_score"])

print("\nMatched Skills:")
print(result["matched_skills"])

print("\nMissing Skills:")
print(result["missing_skills"])