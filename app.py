import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from utils.resume_parser import extract_resume_text
from utils.role_predictor import predict_role
from utils.skill_extractor import extract_skills
from utils.matcher import match_resume_to_job

app = Flask(__name__)

# config
UPLOAD_FOLDER = os.path.join("uploads", "resumes")
ALLOWED_EXTENSIONS = {"txt"}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# create folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Helper function
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# home page
@app.route("/")
def index():
    return render_template("index.html")

# analyze route
@app.route("/analyze", methods = ["POST"])
def analyze():
    if "resume" not in request.files:
        return "No resume file uploaded."
    
    file = request.files['resume']
    job_text = request.form.get("job_text", "").strip()

    if file.filename == "":
        return "No file selected."
    
    if not job_text:
        return "Only .txt resume files are supported for now."
    
    # save uploaded file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    try:
        # extract resume text
        resume_text = extract_resume_text(file_path)

        # predict role
        predicted_role = predict_role(resume_text)

        # extract resume skills
        resume_skills = extract_skills(resume_text)

        # create job skills from job text
        job_skills = extract_skills(job_text)

        # match resume to job
        result = match_resume_to_job(
            resume_text=resume_text,
            job_text=job_text,
            job_skills=job_skills,
            resume_skills=resume_skills
        )

        return render_template(
            "result.html",
            predicted_role = predicted_role,
            resume_text = resume_text,
            resume_skills = resume_skills,
            job_text = job_text,
            job_skills = job_skills,
            tfidf_score = result['tfidf_score'],
            exact_skill_score = result['exact_skill_score'],
            fuzzy_skill_score = result['fuzzy_skill_score'],
            final_score = result['final_score'],
            matched_skills = result['matched_skills'],
            missing_skills = result['missing_skills']
        )
    except Exception as e:
        return f"Error while processing resume: {str(e)}"


# run app
if __name__ == "__main__":
    app.run(debug=True)