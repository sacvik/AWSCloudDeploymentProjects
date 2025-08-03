from fastapi import FastAPI, HTTPException
from app.model import load_model_and_vectorizer, predict_label
from app.schemas import TextRequest, PredictionResponse

app = FastAPI(
    title="Text Multiclass Classifier",
    description="API for multiclass text classification",
    version="1.0.0"
)

model, vectorizer = load_model_and_vectorizer()

@app.post("/predict", response_model=PredictionResponse)
def predict(req: TextRequest):
    try:
        pred = predict_label(req.text, model, vectorizer)
        return PredictionResponse(prediction=pred)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
