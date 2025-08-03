import json
import joblib
from lambda.config import MODEL_PATH, VECTORIZER_PATH

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        text = body.get("text", "")
        if not text:
            return {"statusCode": 400, "body": json.dumps({"error": "No text provided"})}
        X = vectorizer.transform([text])
        pred = model.predict(X)
        return {
            "statusCode": 200,
            "body": json.dumps({"prediction": pred[0]})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
