# Multiclass Text Classification: CI/CD & AWS Deployment

## Overview

- End-to-end pipeline for training, serving, and deploying a multiclass text classifier from Python code to FastAPI/Lambda/AWS with automated CI/CD.
- All configuration is externalized. No code changes needed for retraining or redeployment.

## Project Structure

- `model/`: Model pipeline, training, and config
- `app/`: FastAPI serving REST API
- `lambda/`: AWS Lambda inference function
- `ci_cd/`: Dockerfile, GitHub Actions
- `tests/`: Unit and integration tests

## Local Development

1. **Train Model**
    ```
    pip install -r model/requirements.txt
    python model/train.py
    python model/evaluate.py
    ```

2. **Run FastAPI Locally**
    ```
    pip install -r app/requirements.txt
    uvicorn app.main:app --reload
    ```

3. **Test API**
    ```
    curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"text": "example text"}'
    ```

## CI/CD

- GitHub Actions pipeline automates: train → test → deployment package → (optional) Lambda deploy.
- Any commit to `main` triggers the full pipeline.

## AWS Lambda

- Build Lambda zip as in CI/CD and upload via AWS Console/CLI.
- Use Lambda Layers for larger dependencies/models (see paths in `lambda/config.py`).

---

### Note

- Train/test data and AWS credentials are required separately.
- Adjust config in `model/config.yaml` for your data.
- Add preprocessing, experiment tracking, or advanced models as needed.

---

Built for extensibility and real production usage.
