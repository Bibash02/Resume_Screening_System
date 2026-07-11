# AI Resume Screening & Job Role Prediction System

An AI-powered Resume Screening System built with **Flask** and **Machine Learning** that automatically predicts a candidate's job role and evaluates how well their resume matches a given job description.

This project demonstrates Natural Language Processing (NLP), Machine Learning, Resume Parsing, and Resume-Job Matching in a practical recruitment application.

---

## Features

### Resume Upload
- Upload resumes in:
  - TXT
  - PDF
  - DOCX

### AI Job Role Prediction
Predicts the most suitable job role from the uploaded resume.

Example:

```
Python Developer Resume
        ↓
Predicted Role:
Software Engineer
```

---

### Resume Parsing

Automatically extracts resume text from:

- TXT files
- PDF files
- DOCX files

---

### Skill Extraction

Extracts important skills from the resume such as:

- Python
- Flask
- Django
- SQL
- JavaScript
- Git
- REST API
- Docker
- AWS

---

### Resume-Job Matching

Compares the uploaded resume with a job description using:

- TF-IDF Similarity
- Exact Skill Matching
- Fuzzy Skill Matching

Outputs:

- Match Score
- Matched Skills
- Missing Skills

---

## Machine Learning

### Module 1 — Job Role Prediction

Input:

```
Resume Text
```

Output:

```
Predicted Job Category
```

Example:

```
Data Analyst
Python Developer
HR
Finance
Sales
Consultant
```

Machine Learning Pipeline:

```
Resume Text
      │
      ▼
Text Cleaning
      │
      ▼
TF-IDF Vectorizer
      │
      ▼
Classification Model
      │
      ▼
Predicted Job Role
```

---

### Module 2 — Resume Matching

Inputs:

- Resume
- Job Description

Processing:

```
Resume
        │
        ▼
Extract Skills
        │
        ▼
TF-IDF Similarity
        │
        ▼
Exact Skill Matching
        │
        ▼
Fuzzy Skill Matching
        │
        ▼
Final Matching Score
```

Outputs:

- TF-IDF Score
- Exact Skill Score
- Fuzzy Skill Score
- Final Match Score
- Matched Skills
- Missing Skills

---

## Tech Stack

### Backend

- Python
- Flask

### Machine Learning

- Scikit-learn
- Joblib

### NLP

- TF-IDF Vectorizer
- Cosine Similarity
- RapidFuzz

### Resume Parsing

- pdfplumber
- python-docx

### Frontend

- HTML5
- CSS3
- Jinja2

---

## Project Structure

```
resume_screening_system/
│
├── app.py
├── requirements.txt
├── README.md
│
├── dataset/
│   ├── resumes_dataset.csv
│   └── job_roles_dataset.csv
│
├── model/
│   ├── role_model.pkl
│   ├── tfidf_vectorizer.pkl
│   └── label_encoder.pkl
│
├── uploads/
│   └── resumes/
│
├── utils/
│   ├── matcher.py
│   ├── resume_parser.py
│   ├── role_predictor.py
│   └── skill_extractor.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── css/
│       └── style.css
│
└── notebook/
    ├── role_prediction.ipynb
    └── resume_matching.ipynb
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Bibash02/Resume_Screening_System.git
```

Go into the project

```bash
cd resume_screening_system
```

Create a virtual environment

```bash
python -m venv env
```

Activate it

### Windows

```bash
env\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask server

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## Example Output

### Predicted Role

```
Software Engineer
```

### Matching Scores

```
TF-IDF Score: 81.4

Exact Skill Score: 78.0

Fuzzy Skill Score: 84.5

Final Match Score: 81.2
```

### Matched Skills

```
✔ Python
✔ Flask
✔ Django
✔ SQL
✔ Git
✔ REST API
```

### Missing Skills

```
Docker
AWS
Communication
Leadership
```

---

## Future Improvements

- Resume Database
- Candidate Dashboard
- Recruiter Dashboard
- Resume Ranking
- ATS Score
- Resume Recommendation
- Job Recommendation
- Multiple ML Models Comparison
- Explainable AI (XAI)
- Semantic Search using Sentence Transformers
- OCR Support for Scanned PDF Resumes
- Docker Deployment
- REST API
- Cloud Deployment (Render, Railway, or AWS)

---

## Dataset

This project uses publicly available resume datasets for educational purposes.

Typical fields include:

- Resume Text
- Skills
- Education
- Experience
- Job Category
- Job Description

---
