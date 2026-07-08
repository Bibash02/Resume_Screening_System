import joblib
import os
import numpy as np

# Base path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'model')

# Load save files
model = joblib.load(os.path.join(MODEL_PATH, 'role_model.pkl'))
vectorizer = joblib.load(os.path.join(MODEL_PATH, 'tfidf_vectorizer.pkl'))
label_encoder = joblib.load(os.path.join(MODEL_PATH, 'label_encoder.pkl'))

def clean_text(text):
    import re
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def predict_role(resume_text):
    cleaned = clean_text(resume_text)
    vector = vectorizer.transform([cleaned])
    pred_label = model.predict(vector)[0]
    pred_role = label_encoder.inverse_transform([pred_label])[0]
    return pred_role


