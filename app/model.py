import joblib
import os
from app.config import MODEL_PATH, VECTORIZER_PATH

def load_model_and_vectorizer():
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    return model, vectorizer

def predict_label(text, model, vectorizer):
    vector = vectorizer.transform([text])
    pred = model.predict(vector)
    return pred[0]
